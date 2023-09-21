from django.urls import path
from login_credentials_api import views

urlpatterns = [
    path('keys/', views.CloudLoginViewSet.as_view()),
]
