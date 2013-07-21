from tastypie.authentication import Authentication


class CustomAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.user.is_superuser:
          return True
        return False

    # Optional but recommended
    def get_identifier(self, request):
        return request.user.username