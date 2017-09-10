from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
<<<<<<< HEAD

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
=======
def post_list(request):
    return render(request, 'blog/post_list.html', {})
>>>>>>> 6052b96a2032128a731f1875014bccda0a6d34b3
