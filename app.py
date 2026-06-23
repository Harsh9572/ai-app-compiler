import streamlit as st

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema

from pipeline.validator import validate_app_schema
from pipeline.repair_engine import repair_schema

from pipeline.runtime_generator import generate_runtime
from pipeline.execution_validator import validate_execution

from evaluation.evaluation_runner import run_evaluation

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="AI App Compiler",
    layout="wide"
)

st.title("🤖 AI App Compiler")

st.markdown("""
Natural Language → Intent → Architecture → Schema →
Validation → Repair → Runtime → Execution
""")

# --------------------------------------------------
# Evaluation Dashboard
# --------------------------------------------------

st.header("📊 Evaluation Framework")

if st.button("Run Evaluation Suite"):

    metrics, results = run_evaluation()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Tests",
            metrics["total_tests"]
        )

    with col2:
        st.metric(
            "Success Rate",
            f"{metrics['success_rate']}%"
        )

    with col3:
        st.metric(
            "Repair Rate",
            f"{metrics['repair_rate']}%"
        )

    with col4:
        st.metric(
            "Avg Latency",
            f"{metrics['avg_latency']}s"
        )

    st.subheader("Evaluation Results")

    st.json(results)

st.divider()

# --------------------------------------------------
# Compiler Section
# --------------------------------------------------

st.header("⚙️ Compile Application")

prompt = st.text_area(
    "Describe your application",
    height=150,
    placeholder="""
Example:

Build a CRM with login,
contacts,
dashboard,
payments,
admins can see analytics
"""
)

if st.button("Compile Application"):

    # -----------------------------
    # Stage 1
    # -----------------------------
    intent = extract_intent(prompt)

    # -----------------------------
    # Stage 2
    # -----------------------------
    architecture = design_system(intent)

    # -----------------------------
    # Stage 3
    # -----------------------------
    schema = generate_schema(
        intent,
        architecture
    )

    # -----------------------------
    # Stage 4
    # -----------------------------
    validation = validate_app_schema(
        schema
    )

    # -----------------------------
    # Stage 5
    # -----------------------------
    repaired = False

    if not validation.valid:

        repaired = True

        schema = repair_schema(
            schema,
            validation.errors
        )

        validation = validate_app_schema(
            schema
        )

    # -----------------------------
    # Stage 6
    # -----------------------------
    runtime_file = generate_runtime(
        schema
    )

    # -----------------------------
    # Stage 7
    # -----------------------------
    execution = validate_execution(
        runtime_file
    )

    # --------------------------------------------------
    # Compiler Pipeline Status
    # --------------------------------------------------

    st.header("🚀 Compiler Pipeline")

    st.success("Stage 1 - Intent Extraction")
    st.success("Stage 2 - System Design")
    st.success("Stage 3 - Schema Generation")
    st.success("Stage 4 - Validation")

    if repaired:
        st.warning("Stage 5 - Repair Triggered")
    else:
        st.success("Stage 5 - Repair Not Needed")

    st.success("Stage 6 - Runtime Generation")

    if execution["execution_status"] == "passed":
        st.success("Stage 7 - Execution Validation")
    else:
        st.error("Stage 7 - Execution Failed")

    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Intent")

        st.json(
            intent.model_dump()
        )

        st.subheader("Architecture")

        st.json(
            architecture.model_dump()
        )

    with col2:

        st.subheader("Validation")

        st.json(
            validation.model_dump()
        )

        st.subheader("Execution")

        st.json(
            execution
        )

    st.subheader("Application Schema")

    st.json(
        schema.model_dump()
    )

    with open(runtime_file, "r") as f:

        st.subheader(
            "Generated Runtime"
        )

        st.code(
            f.read(),
            language="python"
        )