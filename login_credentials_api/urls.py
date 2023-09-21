from django.urls import path
from login_credentials_api import views
from .views import enter_account_id, fetch_instances


urlpatterns = [
    path('enter-keys/', views.CloudLoginViewSet.as_view()),
    path('enter-account-id/', enter_account_id, name='enter-account-id'),
    path('fetch-instances/<str:account_id>/', fetch_instances, name='fetch-instances'),
]
