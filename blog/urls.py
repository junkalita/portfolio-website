from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('' , views.home, name='home'),
    path('blog/' , views.BlogListView.as_view(), name='blog_list'),
    # path('blog/' , views.bloglist, name='blog_list'),
    path('<slug:blog_slug>' , views.blogdetail, name='blog_detail')
]
