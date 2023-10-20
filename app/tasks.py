from celery import shared_task
from .models import District
import requests
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)



@shared_task
def process_district(d_id):
    district = District.objects.get(id=d_id)
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={district.lat}&longitude={district.long}&hourly=temperature_2m')
    weather_data = response.json()
    logger.info('weather_data')
    total_temperature = 0
    count = 0

    for i in range(14, 7 * 24, 24):
        total_temperature += weather_data['hourly']['temperature_2m'][i]
        count += 1

    average_temperature = total_temperature / count
    logger.info('average temperature')
    district.avg_temp = average_temperature
    district.save()
    
@shared_task
def daily_task():
    districts = District.objects.values_list('id',flat=True)
    for d_id in districts:
        process_district.delay(d_id)
