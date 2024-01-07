from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.c_language)
admin.site.register(models.java_language)
admin.site.register(models.python_language)