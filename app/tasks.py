from celery import shared_task
from .models import District,DistrictTemperature
import requests
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)



@shared_task
def process_district(d_id):
    logger.info(f'process start for district {d_id}')
    district = District.objects.get(id=d_id)
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={district.lat}&longitude={district.long}&hourly=temperature_2m')
    weather_data = response.json()

    total_temperature = 0
    count = 0

    district_temperature_list = []
    for i in range(14, 7 * 24, 24):
        district_temperature_list.append(DistrictTemperature(district=district,date=weather_data['hourly']['time'][i],temp=weather_data['hourly']['temperature_2m'][i]))
        total_temperature += weather_data['hourly']['temperature_2m'][i]
        count += 1
    DistrictTemperature.objects.bulk_create(district_temperature_list)
    average_temperature = total_temperature / count
    district.avg_temp = average_temperature
    district.save()
    
@shared_task
def daily_task():
    DistrictTemperature.objects.all().delete()
    districts = District.objects.values_list('id',flat=True)
    for d_id in districts:
        process_district.delay(d_id)
    logger.info('all task complete')
