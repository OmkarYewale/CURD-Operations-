from django.urls import path
from . import views
urlpatterns = [
    path("createstudent/",views.Create_student,name="createstudent"),
    path("showallatudent/",views.showallstudent,name="showallatudent"),
    path("updatestudent/<int:id>",views.update,name="updatestudent"),
    path("deletestudent/<int:id>",views.delete,name="deletestudent")
]