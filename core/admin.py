from django.contrib import admin
from .models import Celular,Laptop,PC

# Register your models here.
admin.site.register(Celular)
admin.site.register(Laptop)
admin.site.register(PC)