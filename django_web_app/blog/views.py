from django.shortcuts import render
import django.http
# Create your views here.

posts = [
    {
        'author': "James",
        'title': 'First Blog',
        'content': 'blog content',
        'date_posted': "hardcoded date posted"
    },
    {
        'author': "Not James",
        'title': 'Second Blog',
        'content': 'fake blog content v2',
        'date_posted': "hardcoded date posted that is still wrong"
    }
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About page title'})
