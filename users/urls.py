from django.urls import path
from . import views
from rest_framework.authtoken import views as vAuth

urlpatterns = [
    path("users/register/", views.UserViewRegister.as_view()),
    # path("users/login/", vAuth.obtain_auth_token),
    path("users/login/", views.UserAuthToken.as_view()),
    path("users/", views.UserViewGet.as_view()),
    path("users/<int:user_id>/", views.UserViewOwner.as_view()),
]
