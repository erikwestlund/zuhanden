from orator.migrations import Migration


class CreateRolesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("roles") as table:
            table.big_increments("id")
            table.string("name")
            table.text("description")
            table.timestamps()

        self.db.table("roles").insert(
            [
                {"name": "administrator", "description": "Administrates site."},
                {"name": "user", "description": "Basic site user."},
                {
                    "name": "premium_user",
                    "description": "User with access to premium features.",
                },
            ]
        )

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("roles")
