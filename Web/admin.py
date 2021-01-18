from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Place)
admin.site.register(howToGo)
admin.site.register(Comment)
admin.site.register(List)
admin.site.register(City)
admin.site.register(kind)