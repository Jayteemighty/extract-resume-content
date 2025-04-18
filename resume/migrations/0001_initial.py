# Generated by Django 5.1.7 on 2025-04-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="resumes/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(blank=True, max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=20)),
                ("skills", models.JSONField(default=list)),
                ("experience", models.JSONField(default=list)),
                ("education", models.JSONField(default=list)),
            ],
        ),
    ]
