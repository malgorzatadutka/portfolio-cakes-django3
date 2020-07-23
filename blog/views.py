from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] # najnowsze 5 postów
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
