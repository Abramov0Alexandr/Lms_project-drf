from django.contrib import admin

from subscription.models import CourseSubscription


@admin.register(CourseSubscription)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'is_subscribed',)
    list_editable = ('is_subscribed',)
    list_display_links = ('course',)
