def normalize_intent(data):

    normalized_features = []

    for feature in data.get("features", []):

        feature = feature.lower().strip()

        if "login" in feature or "auth" in feature:
            normalized_features.append("authentication")

        if "contact" in feature:
            normalized_features.append("contacts")

        if "dashboard" in feature:
            normalized_features.append("dashboard")

        if "payment" in feature or "subscription" in feature:
            normalized_features.append("payments")

        if "analytic" in feature:
            normalized_features.append("analytics")

    data["features"] = list(
        dict.fromkeys(normalized_features)
    )

    if not data.get("roles"):
        data["roles"] = ["user"]

    return data