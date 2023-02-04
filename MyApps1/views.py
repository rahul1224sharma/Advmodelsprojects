from django.shortcuts import render
from MyApps1.models import Employees
# Create your views here.

def dis(request):
    employees=Employees.objects.all()
    #employees=Employees.objects.get_emp_sal_range(60000,80000)
    #employees=Employees.objects.get_employees_sorted_by('esal')
    #employees=Employees.objects.get_employees_sorted_by('-esal')
    #employees = Employees.objects.get_employees_sorted_by('-esal')
    #employees = Employees.objects.get_employees_sorted_by('eaddr')
    #employees = Employees.objects.get_employees_sorted_by('-eaddr')
    dict1={'employees':employees}
    return render(request,'MyApps1/index.html',dict1)

from MyApps1.models import ProxyEmployees1,ProxyEmployees2

def d(request):
    #employees=Employees.objects.all()
    #employees=ProxyEmployees1.objects.all()
    employees=ProxyEmployees2.objects.all()
    dict1={'employees':employees}
    return render(request,'MyApps1/index.html',dict1)