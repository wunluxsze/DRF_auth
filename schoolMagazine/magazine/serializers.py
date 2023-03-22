from rest_framework import serializers
from .models import SchoolSubj, Students, SchoolClass

class SchoolSubjSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSubj
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = '__all__'