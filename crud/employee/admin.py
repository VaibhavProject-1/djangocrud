from django.contrib import admin

from employee.forms import EmployeeForm
from employee.models import Employee

# Register your models here.
admin.site.register(Employee)
