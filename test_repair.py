from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema

from pipeline.validator import validate_app_schema
from pipeline.repair_engine import repair_schema

intent = extract_intent(
    "Build CRM with contacts"
)

architecture = design_system(intent)

schema = generate_schema(
    intent,
    architecture
)

# Intentionally break schema
schema.tables = []

print("Before Validation")

result = validate_app_schema(schema)

print(result.model_dump())

if not result.valid:

    schema = repair_schema(
        schema,
        result.errors
    )

    result = validate_app_schema(schema)

    print("After Repair")

    print(result.model_dump())