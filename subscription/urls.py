from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.views import SubscribeToCourse, UnsubscribeFromCourse

app_name = SubscriptionConfig.name


urlpatterns = [
    path('subscribe/<int:course_id>/', SubscribeToCourse.as_view(), name='subscribe'),
    path('unsubscribe/<int:course_id>/', UnsubscribeFromCourse.as_view(), name='unsubscribe'),
]
