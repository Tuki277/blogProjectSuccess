from django.urls import path
from .views import About, Post_Detail, PostList

app_name = 'Home'
urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('<slug:slug>/', Post_Detail.as_view(), name='detail'),
]
