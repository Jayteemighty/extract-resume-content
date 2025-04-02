from rest_framework import serializers
from .models import Resume
import os

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ('uploaded_at', 'name', 'email', 'phone', 'skills', 'experience', 'education')
    
    def validate_file(self, value):
        valid_extensions = ['.pdf', '.doc', '.docx']
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in valid_extensions:
            raise serializers.ValidationError('Unsupported file format. Please upload PDF or Word document.')
        return value