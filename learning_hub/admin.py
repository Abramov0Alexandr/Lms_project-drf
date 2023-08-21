from django.contrib import admin
from .models import Course, Lesson


@admin.register(Course)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_owner',)
    list_editable = ('course_owner',)


@admin.register(Lesson)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'lesson_owner',)
    list_editable = ('lesson_owner',)

