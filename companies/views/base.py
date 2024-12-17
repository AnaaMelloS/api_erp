from rest_framework.views import APIView
from companies.utils.exceptions import NotFoundEmployee, NotFoundGroup, NotFoundTask, NotFoundTaskStatus
from companies.models import Employee, Enterprise, Task, TaskStatus
from accounts.models import Group

import logging
logger = logging.getLogger(__name__)

class Base(APIView):
    def get_enterprise_id(self, user_id):
        employee = Employee.objects.filter(user_id=user_id).first()
        owner = Enterprise.objects.filter(user_id=user_id).first()

        if employee:
            logger.info(f"Usuário {user_id} é funcionário da empresa {employee.enterprise.id}.")
            return employee.enterprise.id

        # Tenta buscar o proprietário da empresa
        owner = Enterprise.objects.filter(user_id=user_id).first()
        if owner:
            logger.info(f"Usuário {user_id} é proprietário da empresa {owner.id}.")
            return owner.id

        # Se nenhum for encontrado, levanta exceção
        logger.error(f"Usuário {user_id} não está associado a nenhuma empresa.")
        raise APIException("Usuário não associado a nenhuma empresa.")

    def get_employee(self, employee_id, user_id):
        enterprise_id = self.get_enterprise_id(user_id)

        employee = Employee.objects.filter(id=employee_id, enterprise_id=enterprise_id).first()

        if not employee:
            raise NotFoundEmployee
        
        return employee
    
    def get_group(self, group_id, enterprise_id):
        group = Group.objects.values('name').filter(id=group_id, enterprise_id=enterprise_id).first()

        if not group:
            raise NotFoundGroup
        
        return group
    
    def get_status(self, status_id):
        status = TaskStatus.objects.filter(id=status_id).first()

        if not status:
            raise NotFoundTaskStatus
        
        return status
    
    def get_task(self, task_id, enterprise_id):
        task = Task.objects.filter(id=task_id, enterprise_id=enterprise_id).first()

        if not task:
            raise NotFoundTask
        
        return task