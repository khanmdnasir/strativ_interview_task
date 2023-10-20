from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

class Coolest10DistricsApi(APIView):
    def get(self,request):        
        pass
        return Response({'success':True})
