from orator.migrations import Migration


class CreateUserOptionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_options") as table:
            table.increments("id")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.json("options")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_options")
