from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    long = models.DecimalField(max_digits=10, decimal_places=8)
    avg_temp = models.DecimalField(max_digits=3, decimal_places=1,default=0)
    
    def __str__(self):
        return self.name