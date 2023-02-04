from django.db import models

# Create your models here.

#Abstract base class Model
class contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    addr=models.CharField(max_length=100)
    class Meta:
        abstract=True

class Student(contact):
    rollno=models.IntegerField()
    mark=models.IntegerField()

class Teacher(contact):
    subject=models.CharField(max_length=60)
    salary=models.FloatField()

#Multi-Table Model

class base(models.Model):
    f1=models.CharField(max_length=30)
    f2 = models.CharField(max_length=30)
    f3 = models.CharField(max_length=30)

class child(base):
    f4 = models.CharField(max_length=30)
    f4 = models.CharField(max_length=30)

#Multi-level Inheritance

class person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()

class Employee(person):
    eno=models.IntegerField()
    esal=models.FloatField()

class Manager(Employee):
    exp=models.IntegerField()
    team_size=models.IntegerField()


#Multiple-Inheritance

class Parent1(models.Model):
    Parent1_id=models.AutoField(primary_key=True)
    f1=models.CharField(max_length=30)
    f2=models.CharField(max_length=30)

class Parent2(models.Model):
    Parent2_id=models.AutoField(primary_key=True)
    f3 = models.CharField(max_length=30)
    f4 = models.CharField(max_length=30)

class C(Parent1,Parent2):
    f5 = models.CharField(max_length=30)
    f6 = models.CharField(max_length=30)

#model.Manager

class Employees(models.Model):
	eno = models.IntegerField()
	ename = models.CharField(max_length = 64)
	esal = models.FloatField()
	eaddr = models.CharField(max_length = 256)

#Custom manager

class CustomManager(models.Manager):
    def get_queryset(set):
        return super().get_queryset.order_by('-eno')

class Employees(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=50)
    object=CustomManager()
    def __str__(self):
        return str(self.eno)+" "+self.ename

#Another Custom Manager

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-eno')

    def get_emp_sal_range(self,esal1,esal2):
        return super().get_queryset().filter(esal__range=(esal1,esal2))

    def get_employees_sorted_by(self,param):
        return super().get_queryset().order_by(param)


#proxy Model
class ProxyEmployees(Employees):
    class Meta():
        proxy=True



class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=70000)

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lt=60000)
class Employees(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=256)
    objects = CustomManager1()
class ProxyEmployees1(Employees):
    objects = CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployees2(Employees):
    objects = CustomManager3()
    class Meta:
        proxy=True