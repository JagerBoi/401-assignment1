from rest_framework import serializers
from base.models import Parts

class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ('id', 'name', 'type', 'price')

class PartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ('id', 'name', 'type', 'release_date',
                   'core_clock', 'clock_unit', 'price', 'TDP', 'part_no')