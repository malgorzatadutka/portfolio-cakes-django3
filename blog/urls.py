from django.urls import path
from . import views

app_name = 'blog' # odwołanie tylko do tej aplikacji w all_blogs

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
   ]