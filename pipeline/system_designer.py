from schemas.architecture import Architecture


def design_system(intent):

    entities = ["User"]

    if "contacts" in intent.features:
        entities.append("Contact")

    if "payments" in intent.features:
        entities.append("Subscription")

    flows = [
        "login",
        "dashboard"
    ]

    modules = [
        "auth",
        "api",
        "database"
    ]

    return Architecture(
        entities=entities,
        flows=flows,
        modules=modules
    )