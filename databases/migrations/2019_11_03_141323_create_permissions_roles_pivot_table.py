from orator.migrations import Migration


class CreatePermissionsRolesPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("permissions_roles") as table:
            table.big_integer("permission_id")
            table.foreign("permission_id").references("id").on("permissions").on_delete(
                "cascade"
            )
            table.big_integer("role_id")
            table.foreign("role_id").references("id").on("roles").on_delete("cascade")

        # Attach permissions to administrator role
        role_administrator = (
            self.db.table("roles").where("name", "administrator").first()
        )

        permission_administrate = (
            self.db.table("permissions").where("name", "administrate").first()
        )

        self.db.table("permissions_roles").insert(
            [
                {
                    "permission_id": permission_administrate.id,
                    "role_id": role_administrator.id,
                }
            ]
        )

        # Attach permissions to user role
        role_user = self.db.table("roles").where("name", "user").first()

        permission_create_blog = (
            self.db.table("permissions").where("name", "create_blog").first()
        )
        permission_create_reference = (
            self.db.table("permissions").where("name", "create_reference").first()
        )
        permission_create_course = (
            self.db.table("permissions").where("name", "create_course").first()
        )
        permission_create_syllabus = (
            self.db.table("permissions").where("name", "create_syllabus").first()
        )

        self.db.table("permissions_roles").insert(
            [
                {"permission_id": permission_create_blog.id, "role_id": role_user.id},
                {
                    "permission_id": permission_create_reference.id,
                    "role_id": role_user.id,
                },
                {"permission_id": permission_create_course.id, "role_id": role_user.id},
                {
                    "permission_id": permission_create_syllabus.id,
                    "role_id": role_user.id,
                },
            ]
        )

        # Attach permissions to premium role.
        role_premium_user = self.db.table("roles").where("name", "premium_user").first()

        permission_use_domain = (
            self.db.table("permissions").where("name", "use_domain").first()
        )

        self.db.table("permissions_roles").insert(
            [
                {
                    "permission_id": permission_use_domain.id,
                    "role_id": role_premium_user.id,
                }
            ]
        )

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("permissions_roles")
