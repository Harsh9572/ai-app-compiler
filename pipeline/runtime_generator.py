from pathlib import Path


def generate_runtime(schema):

    code = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}
"""

    for endpoint in schema.endpoints:

        route = endpoint.path

        func_name = (
            route.replace("/", "_")
            .replace("-", "_")
            .strip("_")
        )

        if not func_name:
            func_name = "root"

        code += f"""

@app.get("{route}")
def {func_name}():
    return {{"endpoint": "{route}"}}
"""

    output_file = Path(
        "runtime/generated/generated_app.py"
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file.write_text(
        code,
        encoding="utf-8"
    )

    return str(output_file)