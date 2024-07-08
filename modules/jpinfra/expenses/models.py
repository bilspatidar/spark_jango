from django.db import models
from django.conf import settings
from django.utils import timezone
from myproject.models import BaseModel
from modules.jpinfra.expense_categories.models import ExpenseCategory
from modules.jpinfra.payment_mode.models import PaymentMode
from modules.jpinfra.machines.models import Machine
from modules.jpinfra.employees.models import Employee
# from modules.jpinfra.projects.models import Project

class Expense(BaseModel):
    title = models.CharField(max_length=255)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expenses')
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE, related_name='expenses')
    admin_remarks = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    parts_name = models.CharField(max_length=255)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='expenses')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='expenses')
    salary_month = models.DateField()
    image = models.ImageField(upload_to='uploads/expenses/')

    def __str__(self):
        return self.title
