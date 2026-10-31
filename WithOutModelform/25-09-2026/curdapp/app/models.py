from django.db import models

# Create your models here.

class StudetnInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_no = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "StudetnInfo"
        

