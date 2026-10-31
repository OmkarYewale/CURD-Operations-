from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
'''
| Field        | Data type     | Validation                        |
| ------------ | ------------- | --------------------------------- |
| `name`       | CharField     | Required, minimum 3 characters    |
| `email`      | EmailField    | Required, valid email             |
| `age`        | IntegerField  | Between 18 and 35                 |
| `course`     | CharField     | Choose from predefined courses    |
| `phone`      | CharField     | Exactly 10 digits                 |
| `address`    | TextField     | Required                          |
| `created_at` | DateTimeField | Automatically store creation time |
'''

class Student(models.Model):

    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.CharField(unique=True,max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(35)])
    COURSE_CHOICES = [
    ('py', 'Python Programming'),
    ('ja', 'Java Programming'),
    ('dj', 'Django Development'),
    ]
    course = models.CharField(max_length=50,choices=COURSE_CHOICES)
    phone = models.CharField(max_length=10,validators=[RegexValidator(regex=r'^[0-9]{10}$',message="Phone must contain exactly 10 digits.")])
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Student"
    




