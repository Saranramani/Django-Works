from  rest_framework import serializers
from .models import TodoClass

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoClass
        fields = ['id','todo','createdOn']