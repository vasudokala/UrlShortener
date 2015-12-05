from rest_framework import serializers
from shortener.models import Urls

class UrlSerializer(serializers.Serializer):

	class Meta:
		model = Urls
		fields=('httpurl','short_id')
	short_id = serializers.CharField()
	httpurl = serializers.CharField()

	def create(self, validated_data):
		return Urls.objects.create(**validated_data)