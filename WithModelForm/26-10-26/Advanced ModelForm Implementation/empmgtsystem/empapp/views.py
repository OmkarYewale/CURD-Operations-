from django.shortcuts import render,redirect
from .form import Employeeform
from .models import Employee

# Create your views here.

def get_empform_page(request):
    empform = Employeeform()
    return render(request,"createemp.html",{"empform":empform})

def create(request):
    empform = Employeeform()

    if request.method == "POST":
        empform=Employeeform(request.POST)
        if empform.is_valid():
            empform.save()
            return render(request,"createemp.html",{"msg":"Thanks for Registration !","empform":empform})
        # else:
        #     empform = Employeeform()
        #     return render(request,"createemp.html",{"msg":empform.errors,"empform":empform})

    return render(request , "createemp.html",{"empform":empform})

def showall_emp_details(request):
    empdb = Employee.objects.all()
    return render(request,"showallemps.html",{"empdb":empdb})


def update(request,employee_code):
    empdb = Employee.objects.get(employee_code=employee_code)
    empform = Employeeform()
    if request.method == 'POST':
        empform = Employeeform(data=request.POST,instance=empdb)
        if empform.is_valid():
            empform.save()
            return render(request,"createemp.html",{"msg":"Employee Details are updated !","empform":empform})
    
    return render(request , "update.html",{"empform":empform,"empdb":empdb})

def delete(request,employee_code):
    Employee.objects.get(employee_code=employee_code).delete()
    return redirect("get_all_emp_details")






