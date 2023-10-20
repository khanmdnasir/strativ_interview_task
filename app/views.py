from rest_framework import status
from .models import District
from .serializers import DistrictSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class Coolest10DistricsApi(APIView):
    def get(self, request):
        districts = District.objects.all().order_by('avg_temp')[:10]
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
