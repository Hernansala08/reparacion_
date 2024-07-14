from django.db import models

# Create your models here.
class Celular(models.Model):
    modelo = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='photos/%Y/%m/%d/')
    descripcion = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.modelo

class Laptop(models.Model):
    modelo = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='photos/%Y/%m/%d/')
    descripcion = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.modelo

class PC(models.Model):
    modelo = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='photos/%Y/%m/%d/')
    descripcion = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.modelo