from django.contrib import admin
from wcube.models import service
# Register your models here.
class serviceAdmin(admin.ModelAdmin):
     list_display = ('service_icon','service_title','service_des')
    
admin.site.register(service, serviceAdmin)
