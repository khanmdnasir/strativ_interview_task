# Generated by Django 4.2.6 on 2023-10-20 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20231020_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('temp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
            ],
            options={
                'indexes': [models.Index(fields=['district', 'date'], name='app_distric_distric_6db5f2_idx')],
            },
        ),
    ]
