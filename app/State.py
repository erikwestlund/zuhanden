class AppState:
    def get(self, request):
        user = request.user()
        state = {
            "user": {
                "name": user.name if user else None,
                "loggedIn": True if user else False,
            }
        }

        return state
