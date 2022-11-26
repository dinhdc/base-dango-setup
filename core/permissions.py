from rest_framework import permissions

# if request user is author, can update or delete object


class IsAuthorUpdate(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if obj.created_by == request.user:
            return True

        return False
