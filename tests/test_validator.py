from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema

from pipeline.validator import (
    validate_app_schema
)

intent = extract_intent(
    "Build CRM with contacts"
)

architecture = design_system(
    intent
)

schema = generate_schema(
    intent,
    architecture
)

result = validate_app_schema(
    schema
)

print(
    result.model_dump()
)