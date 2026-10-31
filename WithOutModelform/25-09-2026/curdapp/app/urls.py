from django.urls import path
from . import views
urlpatterns = [
    path("",views.GetCreteUserp),
    path("createuser/",views.CreateUser,name="createuser"),

    path("Getupdatep/",views.Getupdatep,name="Getupdatep"),
    path("Showuserforupdate/",views.ShowUserforupdate,name="Showuserforupdate"),
    path("updateuser/",views.UpdateUser,name="updateuser"),

    path("Getdeletep/",views.Getdeletep,name="Getdeletep"),
    path("Showuserfordelete/",views.ShowUserfordelete,name="Showuserfordelete"),
    path("deleteuser/",views.DeleteUser,name="deleteuser")
]
