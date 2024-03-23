from rest_framework import permissions

class DisableDangerousMethods(permissions.BasePermission):
    """
    Global permission to disallow all requests for method OPTIONS.
    """

    def has_permission(self, request, view):
        if request.method not in ['GET', 'HEAD', 'POST']:
            return False
        return True