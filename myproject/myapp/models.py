from django.db import models

# Create your models here.
class Employees(models.Model):
    ad = models.CharField(max_length=20, blank=True, null=True)
    soyad = models.CharField(max_length=20, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'employees'