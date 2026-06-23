from schemas.validation import ValidationResult


def validate_app_schema(schema):

    errors = []

    page_names = [
        page.name.lower()
        for page in schema.pages
    ]

    endpoint_paths = [
        ep.path.lower()
        for ep in schema.endpoints
    ]

    table_names = [
        table.name.lower()
        for table in schema.tables
    ]

    if "contacts" in page_names:

        if "/contacts" not in endpoint_paths:

            errors.append(
                "CONTACTS_PAGE_MISSING_ENDPOINT"
            )

    if "/contacts" in endpoint_paths:

        if "contacts" not in table_names:

            errors.append(
                "CONTACTS_ENDPOINT_MISSING_TABLE"
            )

    return ValidationResult(
        valid=len(errors) == 0,
        errors=errors
    )