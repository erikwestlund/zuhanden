from orator.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.big_increments("id")
            table.string("name")
            table.string("email").unique()
            table.string("password")
            table.json("options")
            table.string("remember_token").nullable()
            table.timestamp("verified_at").nullable()
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")
