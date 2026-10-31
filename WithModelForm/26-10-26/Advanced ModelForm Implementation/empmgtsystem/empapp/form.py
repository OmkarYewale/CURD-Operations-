from .models import Employee
from django.forms import ModelForm

class Employeeform(ModelForm):
    class Meta:
        model=Employee
        fields = "__all__"