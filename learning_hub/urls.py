from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apps import LearningHubConfig
from .views import course_views, lesson_views


app_name = LearningHubConfig.name

router = routers.DefaultRouter()
router.register(r'course', course_views.CourseViewSet, basename='course')

urlpatterns = [

    path('lesson/', lesson_views.LessonListApiView.as_view(), name='lesson_list'),

    path('lesson/create', lesson_views.LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/detail/<int:pk>', lesson_views.LessonRetrieveApiView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>', lesson_views.LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', lesson_views.LessonDestroyApiView.as_view(), name='lesson_delete'),

    path('course/token/', course_views.CourseViewSet.as_view({'post': 'get_token'}), name='course_token_obtain_pair'),
    path('lesson/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('lesson/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

            ] + router.urls
