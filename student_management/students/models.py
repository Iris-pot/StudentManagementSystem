from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name='grade'
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
