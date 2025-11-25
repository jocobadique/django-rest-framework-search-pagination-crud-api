from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    Allow only admin to create/update/delete.
    Normal users can only GET.
    """

    def has_permission(self, request, view):

        if request.method in ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]:
            return True

        # Only admins can modify
        user = request.user
        if hasattr(user, "profile") and user.profile.role == "admin":
            return True

        return False
