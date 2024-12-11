from  rest_framework import serializers
from django.utils.timezone import localtime
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at')
        read_only_fields = ('id', 'created_at') 
        
    def get_created_at(self, obj):
        return localtime(obj.created_at).strftime("%Y-%m-%d %H:%M:%S")