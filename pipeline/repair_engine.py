from schemas.app_schema import Table


def repair_schema(schema, errors):

    for error in errors:

        if (
            error
            ==
            "CONTACTS_ENDPOINT_MISSING_TABLE"
        ):

            schema.tables.append(
                Table(
                    name="contacts",
                    columns=[
                        "id",
                        "name"
                    ]
                )
            )

    return schema