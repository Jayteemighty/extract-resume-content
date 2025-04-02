from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Extracted fields
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    skills = models.JSONField(default=list)
    experience = models.JSONField(default=list)
    education = models.JSONField(default=list)
    
    def __str__(self):
        return f"{self.name or 'Anonymous'} - {self.uploaded_at}"