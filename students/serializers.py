from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'cours', 'is_active')

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    srok = serializers.IntegerField()
    srok_otyy = serializers.BooleanField(default=True)

class hafizSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    hafiz = serializers.BooleanField(default=True)
    is_active = serializers.BooleanField(default=True)

class kyrsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    kyrs = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)

