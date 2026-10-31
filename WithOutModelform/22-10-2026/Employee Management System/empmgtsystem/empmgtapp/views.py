from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.

def get_create_page(request):
    return render(request , "create.html")

def create(request):
    if request.method=="POST":
        Employee.objects.create(
            employee_code=request.POST["employee_code"],
            employee_name = request.POST["employee_name"],
            email = request.POST["email"],
            phone = request.POST["phone"],
            technology = request.POST["technology"],
            experience = request.POST["experience"],
            salary = request.POST["salary"],
            city = request.POST["city"],
            status = request.POST["status"]
        )
        return render (request,"create.html",{"msg":"employee created"})
    return render(request,"create.html",{"msg":"method is not match"})

def get_search_page(request):
    return render(request,"showemps.html")

def show_emp_details(request):
    technology = request.GET['technology']

    empdb = Employee.objects.all()
    error=""

    if technology:
        empdb=Employee.objects.filter(technology__icontains=technology).order_by("employee_name")
        print(empdb)
        if not empdb.exists():
            return render(request ,"showemps.html",{"msg":"emp details not found !"})            
    else:
        error="please enter technology "

    return render(request, "showemps.html",{"empdb":empdb,"msg":error})


def get_update_page(request,employee_code):
    empdb = Employee.objects.get(employee_code=employee_code)
    return render(request,"update.html",{"empdb":empdb})


def update(request):
    employee_code=request.POST["employee_code"]
    Employee.objects.filter(employee_code=employee_code).update(
        employee_code = request.POST["employee_code"],
        employee_name = request.POST["employee_name"],
        email = request.POST["email"],
        phone = request.POST["phone"],
        technology = request.POST["technology"],
        experience = request.POST["experience"],
        salary = request.POST["salary"],
        city = request.POST["city"],
        status = request.POST["status"],
    )
    return redirect("get_search_page")

def delete(request ,employee_code):
    Employee.objects.get(employee_code=employee_code).delete()
    return redirect("get_search_page")




    
    

