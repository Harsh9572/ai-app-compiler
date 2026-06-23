import importlib.util


def validate_execution(file_path):

    try:

        spec = importlib.util.spec_from_file_location(
            "generated_app",
            file_path
        )

        module = importlib.util.module_from_spec(
            spec
        )

        spec.loader.exec_module(module)

        return {
            "execution_status": "passed"
        }

    except Exception as e:

        return {
            "execution_status": "failed",
            "error": str(e)
        }