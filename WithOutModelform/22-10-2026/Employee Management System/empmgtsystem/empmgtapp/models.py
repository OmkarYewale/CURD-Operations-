from django.db import models
from django.core.validators import RegexValidator,MinValueValidator

# Create your models here.

class Employee(models.Model):
    employee_code = models.CharField(max_length=10,unique=True)
    employee_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,validators=[RegexValidator(regex=r'^[0-9]{10}$',message="Phone must contain exactly 10 digits.")])
    Choice_technology = [
        ('ja','Java'),
        ('py',"Python"),
        ('dj','Django'),
        ('re','React Js'),
        ('rest','RESTApi'),
        ('sp','Spring Boot'),
        ('php','PHP Programming'),
        ('js','JavaScript')
    ]
    technology = models.CharField(max_length=50,choices=Choice_technology)
    experience = models.DecimalField(max_digits=4,decimal_places=1,validators=[MinValueValidator(0)])
    salary = models.DecimalField(max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)])
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=[('Active','Active'),('Inactive','Inactive')])

    class Meta:
        db_table = "Employee"

