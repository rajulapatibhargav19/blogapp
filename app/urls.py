
from django.urls import  path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('post/<slug:slug>', views.post_page,name='post_page'),
    path('tag/<slug:slug>', views.tag_page,name='tag_page'),
    path('author/<slug:slug>', views.author_page,name='author_page'),
    path('search/', views.search_post,name='search'),
    path('accounts/register', views.register_user,name='register'),
    path('about/', views.about,name='about'),
    path('bookmark_post/<slug:slug>', views.bookmark_post,name='bookmark'),
    path('like_post/<slug:slug>', views.like_post,name='like'),
    path('all_bookmarked_posts/', views.all_bookmarked_posts,name='allbookmarked'),
    path('all_posts/', views.all_posts,name='all_posts'),
    path('all_liked_posts/', views.all_liked_posts,name='all_liked_posts'),
]