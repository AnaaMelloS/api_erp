from rest_framework import permissions
from accounts.models import User_Groups, Group_Permissions
from django.contrib.auth.models import Permission

def check_permission(user, method, permission_to):
    if not user.is_authenticated:
        return False
    
    if user.is_owner:
        return True

    # Determinando o tipo de permissão baseado no método HTTP
    permission_mapping = {
        'POST': 'add_',
        'PUT': 'change_',
        'DELETE': 'delete_',
        'GET': 'view_',
    }

    required_permission = permission_mapping.get(method, 'view_') + permission_to

    groups = User_Groups.objects.filter(user_id=user.id).values_list('group_id', flat=True)

    # Verificar se algum grupo tem a permissão necessária
    for group_id in groups:
        if Group_Permissions.objects.filter(group_id=group_id, permission__codename=required_permission).exists():
            return True
    
    return False

class BasePermission(permissions.BasePermission):
    # Mensagem padrão para todos os casos
    default_message = 'O funcionário não tem permissão para gerenciar esta sessão.'
    
    def __init__(self, permission_to, message=None):
        self.permission_to = permission_to
        self.message = message or self.default_message

    def has_permission(self, request, _view) -> bool:
        # Verifica a permissão com base na função 'check_permission'
        return check_permission(request.user, request.method, permission_to=self.permission_to)

class EmployeesPermission(BasePermission):
    def __init__(self):
        # Permissão específica para employees
        super().__init__(permission_to='employee')

class GroupsPermission(BasePermission):
    def __init__(self):
        # Permissão específica para groups
        super().__init__(permission_to='group')

class GroupsPermissionsPermission(BasePermission):
    def __init__(self):
        # Permissão específica para group permissions
        super().__init__(permission_to='permission')

class TaskPermission(BasePermission):
    def __init__(self):
        # Permissão específica para tasks
        super().__init__(permission_to='task')