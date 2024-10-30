from django.urls import path
from .views import subscription,token,user


urlpatterns = [
    path('subs/',subscription),
    path('token/',token),
    path('user/',user)
]