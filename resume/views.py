from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Resume
from .serializers import ResumeSerializer
from pyresparser import ResumeParser
import tempfile
import os

class ResumeUploadView(APIView):
    parser_classes = (MultiPartParser,)
    
    def post(self, request, format=None):
        serializer = ResumeSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save file first
            resume = serializer.save()
            
            try:
                # Create temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
                    for chunk in resume.file.chunks():
                        tmp.write(chunk)
                    temp_path = tmp.name
                
                # Parse resume
                data = ResumeParser(temp_path).get_extracted_data()
                
                # Update model
                resume.name = data.get('name', '')
                resume.email = data.get('email', '')
                resume.phone = data.get('mobile_number', '')
                resume.skills = data.get('skills', [])
                resume.experience = data.get('experience', [])
                resume.education = data.get('education', [])
                resume.save()
                
                # Clean up
                os.unlink(temp_path)
                
                return Response({
                    'success': True,
                    'resume_id': resume.id,
                    'data': {
                        'name': resume.name,
                        'email': resume.email,
                        'phone': resume.phone,
                        'skills': resume.skills,
                        'experience': resume.experience,
                        'education': resume.education
                    }
                }, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                # Clean up on error
                if 'temp_path' in locals() and os.path.exists(temp_path):
                    os.unlink(temp_path)
                resume.file.delete()
                resume.delete()
                return Response({
                    'success': False,
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)