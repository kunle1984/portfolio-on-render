from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class myUser(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    image = models.ImageField(null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
   # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Project(models.Model):
    user=models.ForeignKey(myUser,  on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    image=models.ImageField(upload_to='project_images')
    slug=models.SlugField(unique=True)
    project_link=models.CharField(max_length=200, null=True, blank=True)
    github_link=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-({self.category})'


class Blog(models.Model):
    user=models.ForeignKey(myUser,  on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField()
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    image=models.ImageField(upload_to='blog_images')
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-({self.category})'

class Project_upload(models.Model):
    user=models.ForeignKey(myUser,  on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    image=models.ImageField(upload_to='project_images')

    def __str__(self):
        return f'{self.title}-({self.category})'
