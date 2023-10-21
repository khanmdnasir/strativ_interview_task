from rest_framework import status
from .models import District, DistrictTemperature
from .serializers import DistrictSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class Coolest10DistricsApi(APIView):
    def get(self, request):
        districts = District.objects.all().order_by('avg_temp')[:10]
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RecomendationApi(APIView):
    def get(self, request):
        if 'location' not in self.request.query_params:
            return Response({"message": "Select your location"}, status=status.HTTP_400_BAD_REQUEST)
        if 'destination' not in self.request.query_params:
            return Response({"message": "Select destination"}, status=status.HTTP_400_BAD_REQUEST)
        if 'date' not in self.request.query_params:
            return Response({"message": "Select date when you want to travel"}, status=status.HTTP_400_BAD_REQUEST)
        date_str = str(str(self.request.query_params.get('date'))+"T14:00")
        location_temperature = DistrictTemperature.objects.filter(
            district=self.request.query_params.get('location'), date=date_str).first()
        destination_temperature = DistrictTemperature.objects.filter(
            district=self.request.query_params.get('destination'), date=date_str).first()
        temp_list = list(District.objects.values(
            'avg_temp').order_by('avg_temp')[:10])
        
        min_temp = temp_list[0]['avg_temp']
        max_temp = temp_list[-1]['avg_temp']

        if location_temperature is None or destination_temperature is None:
            return Response({"message": "Data not available for the specified date."}, status=status.HTTP_404_NOT_FOUND)
        if min_temp <= location_temperature.temp < max_temp and min_temp <= destination_temperature.temp < max_temp:
            recomendation = "Both locations are cool. Enjoy your trip!"
        elif min_temp <= destination_temperature.temp <= max_temp:
            recomendation = "The destination is cool. It's a good time to travel!"
        elif min_temp <= location_temperature.temp < max_temp:
            recomendation = "Your location is cool. You may not need to travel."
        else:
            recomendation = "No coolest districts found. Use your preference to decide."
        return Response({"location_temp": location_temperature.temp, "destination_temp": destination_temperature.temp, "recomendation": recomendation, }, status=status.HTTP_200_OK)
