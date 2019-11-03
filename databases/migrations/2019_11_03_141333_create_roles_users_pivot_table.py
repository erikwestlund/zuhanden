from orator.migrations import Migration


class CreateRolesUsersPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("roles_users") as table:
            table.big_integer("user_id")
            table.foreign("user_id").references("id").on("users").on_delete("cascade")
            table.big_integer("role_id")
            table.foreign("role_id").references("id").on("roles").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("roles_users")
