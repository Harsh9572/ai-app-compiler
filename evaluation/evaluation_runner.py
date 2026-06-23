import json
import time

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_app_schema
from pipeline.repair_engine import repair_schema
from pipeline.runtime_generator import generate_runtime
from pipeline.execution_validator import validate_execution


def run_evaluation():

    with open(
        "evaluation/dataset.json",
        "r",
        encoding="utf-8"
    ) as f:

        dataset = json.load(f)

    total = len(dataset)

    successes = 0
    repairs = 0

    latencies = []

    results = []

    for item in dataset:

        start = time.time()

        try:

            prompt = item["prompt"]

            intent = extract_intent(prompt)

            architecture = design_system(intent)

            schema = generate_schema(
                intent,
                architecture
            )

            validation = validate_app_schema(
                schema
            )

            if not validation.valid:

                repairs += 1

                schema = repair_schema(
                    schema,
                    validation.errors
                )

            runtime_file = generate_runtime(
                schema
            )

            execution = validate_execution(
                runtime_file
            )

            if (
                execution["execution_status"]
                ==
                "passed"
            ):
                successes += 1

            latency = (
                time.time() - start
            )

            latencies.append(
                latency
            )

            results.append(
                {
                    "prompt": prompt,
                    "status":
                    execution[
                        "execution_status"
                    ]
                }
            )

        except Exception as e:

            results.append(
                {
                    "prompt": item["prompt"],
                    "status": "failed",
                    "error": str(e)
                }
            )

    metrics = {

        "total_tests": total,

        "success_rate":
        round(
            (successes / total) * 100,
            2
        ),

        "repair_rate":
        round(
            (repairs / total) * 100,
            2
        ),

        "avg_latency":
        round(
            sum(latencies)
            / len(latencies),
            4
        )
        if latencies
        else 0
    }

    return metrics, results