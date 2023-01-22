from django.contrib import admin
from todoapp.models import Contact
from todoapp.models import Task
from todoapp.models import Owner

# Register your models here.

admin.site.register(Contact)
admin.site.register(Task)
admin.site.register(Owner)
