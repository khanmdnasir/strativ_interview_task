# Generated by Django 4.2.6 on 2023-10-20 09:30

from django.db import migrations
import requests


def add_initial_data(apps, schema_editor):
    District = apps.get_model('app', 'District')
    response = requests.get(
        'https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json')
    data = response.json()
    district_to_insert = [District(
        name=i['name'], lat=i['lat'], long=i['long']) for i in data['districts']]
    District.objects.bulk_create(district_to_insert)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
