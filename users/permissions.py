from rest_framework import permissions


class IsOwnerOrAdminAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_employee


class IsAdminAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_employee
