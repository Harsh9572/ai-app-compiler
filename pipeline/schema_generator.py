from schemas.app_schema import (
    AppSchema,
    Page,
    Table,
    Endpoint,
    Role
)


def generate_schema(intent, architecture):

    pages = [
        Page(
            name="Dashboard",
            route="/dashboard"
        )
    ]

    if "contacts" in intent.features:

        pages.append(
            Page(
                name="Contacts",
                route="/contacts"
            )
        )

    tables = [
        Table(
            name="users",
            columns=[
                "id",
                "email"
            ]
        )
    ]

    if "Contact" in architecture.entities:

        tables.append(
            Table(
                name="contacts",
                columns=[
                    "id",
                    "name"
                ]
            )
        )

    endpoints = [
        Endpoint(
            path="/users",
            method="GET"
        )
    ]

    if "Contact" in architecture.entities:

        endpoints.append(
            Endpoint(
                path="/contacts",
                method="GET"
            )
        )

    roles = [
        Role(
            name="user",
            permissions=["view"]
        )
    ]

    if "admin" in intent.roles:

        roles.append(
            Role(
                name="admin",
                permissions=["all"]
            )
        )

    return AppSchema(
        app_name="Generated App",
        pages=pages,
        tables=tables,
        endpoints=endpoints,
        roles=roles,
        business_rules=[]
    )