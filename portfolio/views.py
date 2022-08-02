from unicodedata import category
from django.shortcuts import render
from .models import *
import os
from .forms import ContactForm
from django.http.response import HttpResponse
import mimetypes
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
# Create your views here.

def index(request):

    projects=Project.objects.all()
    form=ContactForm()
    
    return render(request, 'portfolio/index.html', {'projects':projects, 'form':form})
  

def projects(request):
   
    return render(request, 'portfolio/project.html')
  
def blog(request):
    category=request.GET.get('category')
    if category== None:
        blogs=Blog.objects.all()
        blogs=blogs.order_by('-id')
       
    else:
         blogs=Blog.objects.filter(category__name__icontains=category)
    categories=Category.objects.all()[:8]
    return render(request, 'portfolio/blog.html', {'blogs':blogs, 'categories':categories})

def blog_by_category(request, category):
    
    if category== None:
        blogs=Blog.objects.filter(category__name=category)
    else:
         blogs=Blog.objects.filter(category__name__icontains=category)
    categories=Category.objects.all()[:8]
    return render(request, 'portfolio/blog_by_category.html', {'blogs':blogs, 'categories':categories})


def project_view(request, portfolio_slug):
    project=Project.objects.get(slug=portfolio_slug)
    more_images=Project_upload.objects.filter(category=project.category.id)
   
    context={'project':project, 'images':more_images}
    return render(request, 'portfolio/project_view.html' , context)


def blog_view(request, blog_slug):
    blog=Blog.objects.get(slug=blog_slug)
    blogs=Blog.objects.all()
    categories=Category.objects.all()
    context={'blogs':blogs, 'blog':blog, 'categories':categories}
    return render(request, 'portfolio/blog_view.html',context )

def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/portfolio/static/portfolio/file/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'index.html')
  
  
class Contact(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')