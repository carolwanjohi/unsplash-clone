from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    '''
    Class that only allows users with admin privileges to perform certain requests
    '''
    def has_permission(self, request, view):
        '''
        Checks if the request belongs to SAFE_METHODS
        Prevents any request other than SAFE_METHODS to be executed by Admin only
        '''
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff