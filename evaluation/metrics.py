from evaluation.evaluation_runner import (
    run_evaluation
)


def get_metrics():

    metrics, _ = run_evaluation()

    return metrics