from django.contrib import admin
from MyApps1.models import Employees,ProxyEmployees1,ProxyEmployees2

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employees,EmployeesAdmin)

#proxy admin
class Proxyadmin1(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr'];

admin.site.register(ProxyEmployees1,Proxyadmin1)


class Proxyadmin2(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr'];

admin.site.register(ProxyEmployees2,Proxyadmin2)