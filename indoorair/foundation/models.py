from django.db import models
from django.contrib.auth.models import User



class Instrument(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name + " " + str(self.user)




class Sensor(models.Model):
    name = models.CharField(max_length=255)
    instrument = models.ForeignKey(
        to='Instrument',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name +" " + str(self.instrument)




class TimeSeriesDatum(models.Model):
    value = models.FloatField()
    time = models.DateTimeField()
    instrument = models.ForeignKey(
        to='Sensor',
        on_delete=models.CASCADE
    )
    value = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.sensor) +''+ str(self.value)



class Data(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    co2 = models.FloatField()
    tvoc = models.FloatField()
    humidity = models.FloatField()
