from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    kurs = models.PositiveIntegerField()
    raqam = models.PositiveIntegerField()

class Reja(models.Model):
    sarlavha = models.CharField(max_length=30)
    sanasi = models.DateField()
    batafsil = models.CharField(max_length=500)
    bajarilgan = models.BooleanField()
    student = models.ForeignKey(Talaba, on_delete=models.CASCADE)