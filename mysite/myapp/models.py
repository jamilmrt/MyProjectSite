from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='project_images/')
    project_link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.project_name}"
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    