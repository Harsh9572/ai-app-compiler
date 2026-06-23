from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema

from pipeline.runtime_generator import (
    generate_runtime
)

from pipeline.execution_validator import (
    validate_execution
)

intent = extract_intent(
    "Build CRM with contacts"
)

architecture = design_system(intent)

schema = generate_schema(
    intent,
    architecture
)

runtime_file = generate_runtime(
    schema
)

print(
    validate_execution(runtime_file)
)