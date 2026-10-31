from .models import Student

from django.forms import ModelForm

class stdmodelform(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'