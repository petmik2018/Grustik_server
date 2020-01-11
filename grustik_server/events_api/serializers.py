from events_api import models
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)


    class Meta:
        model = models.Event
        fields = ('id', 'title', 'description', 'location', 'date',)
        read_only_fields = ('id',)

