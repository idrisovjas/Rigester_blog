from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,TemplateView


# Create your views here.

class PostView(ListView):
    model = Post

    template_name = 'home.html'

class Tasnif(TemplateView):
    template_name = 'bosh.html'


class admin(TemplateView):
    template_name = 'admin.html'


class Qosh(DetailView):
    model = Post
    template_name = 'bosh.html'


