from django.shortcuts import render,redirect
from .modleform import stdmodelform
from .models import Student

# Create your views here.

def Create_student(request):
    form = stdmodelform()

    if request.method == "POST":
        form = stdmodelform(request.POST)

        if form.is_valid():
            form.save()
            std=Student.objects.all().last()
            return render(request,"create.html",{"form":form,"std":std})
        else:
            form=stdmodelform()

    return render(request,"create.html",{"form":form})

def showallstudent(request):
    stddb = Student.objects.all()
    return render(request,"showallstudents.html",{"stddb":stddb})

def update(request ,id):
    stddb = Student.objects.get(id=id)
    form = stdmodelform()
    if request.method =="POST":
        form = stdmodelform(data=request.POST,instance=stddb)
        if form.is_valid():
            form.save()
            return redirect("showallatudent")
    return render(request,"update.html",{"stddb":stddb,"form":form})

def delete(request,id):
    Student.objects.get(id=id).delete()
    return redirect("showallatudent")
