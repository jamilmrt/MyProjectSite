from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.

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
    
    
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    person_name = models.CharField(max_length=100)
    person_image = models.ImageField(upload_to='person_images/')
    # person_description = models.TextField()
    person_bio = models.CharField(max_length=255, null=True, blank=True, default="No biography provided.") # Write about Author shortly
    person_phone = models.CharField(max_length=20)
    person_email = models.EmailField(null=True, blank=True, default="")
    person_github = models.URLField(null=True, blank=True, default="")
    person_linkedin = models.URLField(null=True, blank=True, default="")
    person_twitter = models.URLField(null=True, blank=True, default="")
    person_facebook = models.URLField(null=True, blank=True, default="")
    person_instagram = models.URLField(null=True, blank=True, default="")
    person_website = models.URLField(null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.person_name}"