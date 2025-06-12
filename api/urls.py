from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import public_view, protected_view, run_test_task

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('login/', obtain_auth_token),
    path('run-task/', run_test_task),
]
