from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from resume.views import ResumeUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/resumes/', ResumeUploadView.as_view(), name='resume-upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)