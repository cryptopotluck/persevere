from django.shortcuts import render

# Create your views here.
def blog_home(requests):
    return render(requests, 'blog/blog_home.html')