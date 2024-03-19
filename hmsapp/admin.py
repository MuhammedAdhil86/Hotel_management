from django.contrib import admin
from .models import staff,customer,room
# Register your models here.
admin.site.register(staff)
admin.site.register(customer)
admin.site.register(room)