from django.urls import path
from .views import Coolest10DistricsApi
urlpatterns = [
    path('coolest_10_districts',Coolest10DistricsApi.as_view())
]