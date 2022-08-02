from django.urls import path
from . import views
from .views import Contact
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('projects', views.projects, name='project'),
    path('projects/<str:portfolio_slug>', views.project_view, name='project-view'),
    path('blogs', views.blog, name='blogs'),
    path('success', views.contact_success, name='contact-success'),
    path('blog-view/<str:blog_slug>', views.blog_view, name='blog-view'),
    path('download/<str:filename>', views.download_file, name='download'),
    path('contact', Contact.as_view(), name='contact'),
    path('blog-by-category/<str:category>', views.blog_by_category, name='blog-by-category'),
  
]

