from pydantic import BaseModel

from schemas.intent import Intent
from schemas.architecture import Architecture
from schemas.app_schema import AppSchema


class CompilerOutput(BaseModel):

    intent: Intent

    architecture: Architecture

    schema: AppSchema

    validation_passed: bool