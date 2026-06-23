from evaluation.evaluation_runner import (
    run_evaluation
)

metrics, results = run_evaluation()

print(metrics)

for result in results:

    print(result)