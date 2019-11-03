from orator.migrations import Migration


class CreatePermissionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("permissions") as table:
            table.big_increments("id")
            table.string("name")
            table.text("description")
            table.timestamps()

        self.db.table("permissions").insert(
            [
                {"name": "administrate", "description": "Allowed to administrate site"},
                {"name": "create_blog", "description": "Allowed to create a blog."},
                {
                    "name": "create_reference",
                    "description": "Allowed to create references.",
                },
                {"name": "create_course", "description": "Allowed to create courses."},
                {
                    "name": "create_syllabus",
                    "description": "Allowed to create syllabuses.",
                },
                {
                    "name": "use_domain",
                    "description": "Allowed to use a domain name for public pages.",
                },
            ]
        )

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("permissions")
