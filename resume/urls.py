from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.ResumeUploadView.as_view(), name='resume-upload'),
]