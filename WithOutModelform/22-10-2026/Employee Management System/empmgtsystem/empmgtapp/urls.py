from django.urls import path,include
from . import views
urlpatterns = [
    path("getcreatepage/",views.get_create_page),
    path("create/",views.create,name="create"),
    path("get_search_page/",views.get_search_page,name="get_search_page"),
    path("searchemp/",views.show_emp_details,name="searchemp"),
    path("get_update_page/<str:employee_code>/",views.get_update_page,name="get_update_page"),
    path("update/",views.update,name="update"),
    path("delete/<str:employee_code>/",views.delete,name="delete")
]
