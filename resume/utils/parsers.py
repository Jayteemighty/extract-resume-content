import os
import tempfile
from resume_parser import parse_resume

class ResumeParser:
    @staticmethod
    def parse(file):
        """Parse resume file and return extracted data"""
        try:
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp:
                for chunk in file.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name
            
            # Parse the resume
            data = parse_resume(tmp_path)
            
            # Clean up temp file
            os.unlink(tmp_path)
            
            return {
                'name': data.get('name', ''),
                'email': data.get('email', ''),
                'phone': data.get('phone', ''),
                'skills': data.get('skills', []),
                'experience': data.get('experience', []),
                'education': data.get('education', []),
            }
        except Exception as e:
            raise ValueError(f"Resume parsing failed: {str(e)}")