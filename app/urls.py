from django.urls import path
from .views import Coolest10DistricsApi,RecomendationApi
urlpatterns = [
    path('coolest_10_districts',Coolest10DistricsApi.as_view()),
    path('recomendation',RecomendationApi.as_view())
]