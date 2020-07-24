from django.shortcuts import render
from django.views import View, generic
from .models import Post

# Create your views here.

class About(View):
    def get(self, request):
        return render(request, 'homepage/about.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'homepage/index.html'


class Post_Detail(generic.DetailView):
    model = Post
    template_name = 'homepage/post_detail.html'
