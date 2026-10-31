from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    stock_count = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return self.title
