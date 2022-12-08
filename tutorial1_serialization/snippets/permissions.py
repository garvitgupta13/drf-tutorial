from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to anly allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        """
        OPTIONS method returns info about API (methods/content type)
        HEAD method returns info about resource (version/length/type)
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
