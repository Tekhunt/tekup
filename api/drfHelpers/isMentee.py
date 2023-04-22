from rest_framework.permissions import BasePermission


class IsMentee(BasePermission):
    message = "You must be a mentee to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_mentee
