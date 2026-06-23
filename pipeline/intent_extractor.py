import time

from schemas.intent import Intent
from pipeline.gemini_client import client
from pipeline.json_utils import extract_json
from pipeline.intent_normalizer import normalize_intent


SYSTEM_PROMPT = """
You are an Intent Extraction Engine.

Convert the user's application request into JSON.

Return ONLY valid JSON.

Schema:

{
  "app_type": "string",
  "features": [],
  "roles": [],
  "constraints": []
}
"""


AVAILABLE_MODELS = [
    "gemini-2.5-flash"
]


def fallback_extractor(user_prompt: str):

    prompt = user_prompt.lower()

    features = []

    if "login" in prompt:
        features.append("authentication")

    if "dashboard" in prompt:
        features.append("dashboard")

    if "contact" in prompt:
        features.append("contacts")

    if "payment" in prompt:
        features.append("payments")

    if "analytic" in prompt:
        features.append("analytics")

    roles = ["user"]

    if "admin" in prompt:
        roles.append("admin")

    return Intent(
        app_type="custom_app",
        features=features,
        roles=roles,
        constraints=[]
    )


def extract_intent(user_prompt: str):

    prompt_text = f"""
{SYSTEM_PROMPT}

USER REQUEST:
{user_prompt}
"""

    for model_name in AVAILABLE_MODELS:

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt_text
                )

                data = extract_json(
                    response.text
                )

                data = normalize_intent(
                    data
                )

                return Intent(**data)

            except Exception:

                time.sleep(2)

    print(
        "Primary AI unavailable. Using fallback extractor."
    )

    return fallback_extractor(
        user_prompt
    )