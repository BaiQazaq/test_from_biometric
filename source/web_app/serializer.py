from rest_framework import serializers
from web_app.models import People

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ('name', 'inn', 'age', 'created_at', 'changed_at')
        read_only_fields = ('id', 'created_at', 'changed_at')

    def update(self, instance, validated_data):
        print("SERIALIZER+++", instance, "+", validated_data)
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance