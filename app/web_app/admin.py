from django.contrib import admin
from app.web_app.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'address', 'warehouse_address']
    list_filter = ['id', 'full_name', 'phone_number', 'address', 'warehouse_address']
    search_fields = ['id', 'full_name', 'phone_number']