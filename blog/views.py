from django.shortcuts import render, get_object_or_404 #jeśli nie ma obiektu to error 404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] # najnowsze 5 postów
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
 
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #primary key z bazy danych, to numer wpisu na blogu
    return render(request, 'blog/detail.html',{'blog':blog}) # odwołanie do strony detail.html, blog_id pojawia się w blog-> urls