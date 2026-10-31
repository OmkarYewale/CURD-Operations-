from django.urls import path,include
from . import views
urlpatterns = [
    path("get_createemp_page/",views.get_empform_page,name="get_createemp_page"),
    path("create/",views.create,name="create"),
    path("get_all_emp_details/",views.showall_emp_details,name="get_all_emp_details"),
    path("update/<str:employee_code>/",views.update,name="Update"),
    path("Delete/<str:employee_code>/",views.delete,name="Delete")
    
]