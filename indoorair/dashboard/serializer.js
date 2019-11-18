"""
api/serializers.py
"""
from rest_framework import serializers # (1) NEED TO IMPORT CLASS
from rest_framework.validators import UniqueTogetherValidator
from foundation.models import Data # (2) OPTIONAL - IMPORT ANY MODELS WE USE


MEMORY_ID = 0

class AvgSeriliazer(serializers.Serializer):
    value = serializers.FloatField()
    def create(self, validated_data):
        try:
            memory = Data.object.get(id=MEMORY_ID)
        except Data.DoesnotExist:
            memory = Data.object.create(
                id = MEMORY_ID,
                avg_temperature = 0,
                avg_pressure = 0,
                avg_co2 = 0,
                avg_tvoc = 0,
                avg_humidity  = 0,
            )
        avg_temperature = validated_data.get('avg_temperature')
        avg_pressure = validated_data.get('avg_pressure')
        avg_co2 = validated_data.get('avg_co2')
        avg_tvoc = validated_data.get('avg_tvoc')
        avg_humidity = validated_data.get('avg_humidity')
        memory.avg_temperature = (memory.temperature + avg_temperature)/2
        memory.avg_pressure = (memory.pressure + avg_pressure)/2
        memory.avg_co2 = (memory.co2 + avg_co2)/2
        memory.avg_tvoc = (memory.tvoc + avg_tvoc)/2
        memory.avg_humidity = (memory.temperature + avg_humidity)/2
        memory.save()

        return memory
