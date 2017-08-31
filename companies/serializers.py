from rest_framework import serializers
from .models import Farmerinfo
from django.db import models


class FarmerinfoSerializer(serializers.ModelSerializer):

	farmer_id = models.IntegerField()
	farmer_name = models.CharField(max_length=30)
	farmer_village = models.CharField(max_length=25)
	farmer_farms = models.IntegerField()

	class Meta:
		model = Farmerinfo
		fields = '__all__'
	
	def create(self, validated_data):
#		Create and return a new `Farmerinfo` instance, given the validated data.
		return Farmerinfo.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Farmerinfo` instance, given the validated data.
		"""
		instance.farmer_id = validated_data.get('farmer_id', instance.farmer_id)
		instance.farmer_name = validated_data.get('farmer_name', instance.farmer_name)
		instance.farmer_village = validated_data.get('farmer_village', instance.farmer_village)
		instance.farmer_farms = validated_data.get('farmer_farms', instance.farmer_farms)
		instance.save()
		return instance