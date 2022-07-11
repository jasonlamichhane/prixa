from django.contrib import admin
from .models import ServerDetails
# Register your models here.

@admin.register(ServerDetails)
class ServerDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','servername','servertype','disktype','owner','serverlocation','cpu','ram','ipaddress','username','password','publicip','privateip','remarks','status')
    