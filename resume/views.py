from rest_framework import generics, status
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer
from .utils.parsers import ResumeParser

class ResumeUploadView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            # Save resume file first
            resume = serializer.save()
            
            # Parse the resume
            parser = ResumeParser()
            parsed_data = parser.parse(resume.file)
            
            # Update the model with parsed data
            for field, value in parsed_data.items():
                setattr(resume, field, value)
            resume.save()
            
            return Response(
                self.get_serializer(resume).data,
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            # Clean up if parsing fails
            if 'resume' in locals():
                resume.file.delete()
                resume.delete()
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )