from rest_framework.permissions import BasePermission


class IsMentor(BasePermission):
    message = "You must be a mentor to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_mentor
