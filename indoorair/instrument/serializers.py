from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from foundation.models import Instrument, Sensor, TimeSeriesDatum


class InstrumentSerializer(serializers.Serializer):


    id = serializers.IntegerField()
    location = serializers.CharField()
    serial_number = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data):

        location = validated_data.get('location', None)
        instrument = Instrument.objects.create(location=location)
        return instrument


    def update(self, object, validated_data):

        object.url = validated_data.get('url')
        object.save()
        return object
