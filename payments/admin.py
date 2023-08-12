from django.contrib import admin
from payments.models import Payments


@admin.register(Payments)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payments._meta.get_fields()]
    list_display_links = ('user',)
