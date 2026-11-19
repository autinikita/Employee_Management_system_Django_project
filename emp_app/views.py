from django.shortcuts import render ,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Add(request):
    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept = Department.objects.get(id=request.POST['dept'])
        role = Role.objects.get(id=request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept=dept, role=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added sucessfully")
    elif request.method=='GET':
        return render(request, 'Add.html')
    else:
        return HttpResponse("An exception occured! Employee has not been added")

def Remove(request, emp_id = 0):
    if emp_id:
        try:
           emp_to_be_Remove = Employee.objects.get(id=emp_id)
           emp_to_be_Remove.delete()
           return HttpResponse("Employee Removed Sucessfully")
        except:
            return HttpResponse("please enter a valid emp_id")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'Remove.html', context)

def All_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'All_emp.html', context)


def filter_emp(request):
    emps = Employee.objects.all()

    if request.method == "GET":
        name = request.GET.get('first_name')
        dept = request.GET.get('dept')
        role = request.GET.get('role')

        if name:
            emps = emps.filter(
                Q(first_name__icontains=name) |
                Q(last_name__icontains=name)
            )

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'All_emp.html', context)

    return render(request, 'filter_emp.html')



# def filter_emp(request):
#     name=request.POST['name']
#     dept=request.POST['dept']
#     role=int(request.POST['role'])
#     emps = Employee.objects.all()
#     if name:
#        emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))   
#     if dept:
#         emps = emps.filter(dept__name = dept)
#     if role:
#         emps = emps.filter(role__name = role)
        
#         context = {
#             'emps': emps
#             }
#         return render(request, 'All_emp.html', context)
#     elif request.method =='GET':
#         return render(request, 'filter_emp.html')
#     else:
#         return HttpResponse('An Exception occured')
