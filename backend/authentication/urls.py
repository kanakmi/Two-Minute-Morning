from django.urls import path
from .views import *
urlpatterns = [
    path('login/',signin),
    path("login/ajax/",signin_ajax),
    path('signup/',signup),
    path('signout/',signout),
]