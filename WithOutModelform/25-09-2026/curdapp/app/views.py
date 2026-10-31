from django.shortcuts import render
from .models import StudetnInfo
# Create your views here.

def GetCreteUserp(request):
    return render(request,"create.html")

def CreateUser(request):
    if request.method =='POST':
        StudetnInfo.objects.create(
            name = request.POST['name'],
            age = request.POST['age'],
            mobile_no = request.POST['mobile_no']
        )
        return render(request,"create.html",{"msg":"User Created !!!"})
    else:
        return render(request,"create.html",{"msg":"something missing !!!"})

def Getupdatep(request):
    return render(request,"update.html")

def ShowUserforupdate(request):
    id  = request.POST['id']

    sdb = StudetnInfo.objects.get(id = id)

    return render(request,"update.html",{'sdb':sdb})

def UpdateUser(request):
    id = request.POST['id']

    if request.method == 'POST':
        if id:
            StudetnInfo.objects.filter(id = id).update(
                id = request.POST['id'],
                name = request.POST['name'],
                age = request.POST['age'],
                mobile_no = request.POST['mobile_no']
            )
            return render(request,"update.html",{"msg":"User info Updated !!!"})
        else:
            return render(request,"update.html")

def Getdeletep(request):
    return render(request,"delete.html")

def ShowUserfordelete(request):
    id  = request.POST['id']

    sdb = StudetnInfo.objects.get(id = id)

    return render(request,"delete.html",{'sdb':sdb})

def DeleteUser(request):
    id = request.POST['id']
    StudetnInfo.objects.filter(id = id).delete()

    return render(request,"delete.html",{"msg":"User deleted"})
