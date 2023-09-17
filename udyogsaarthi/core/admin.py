from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Issues)
admin.site.register(models.Course)
admin.site.register(models.Job)
admin.site.register(models.Enrolledcourse)
