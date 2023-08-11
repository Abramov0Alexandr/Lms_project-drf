from rest_framework import routers
from django.urls import path
from .views import course_views, lesson_views
from .apps import LearningHubConfig


app_name = LearningHubConfig.name

router = routers.DefaultRouter()
router.register(r'course', course_views.CourseViewSet, basename='course')

urlpatterns = [

    path('lesson', lesson_views.LessonListApiView.as_view(), name='lesson_list'),

    path('lesson/create', lesson_views.LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/detail/<int:pk>', lesson_views.LessonRetrieveApiView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>', lesson_views.LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', lesson_views.LessonDestroyApiView.as_view(), name='lesson_delete'),

] + router.urls
