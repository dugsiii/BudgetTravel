from rest_framework import serializers
from trip_history.models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'StayedHotel', 'TripPeriod', 'Activities', 'TotalCost']