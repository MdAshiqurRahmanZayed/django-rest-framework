from rest_framework import serializers
from ToDo.models import ToDo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'