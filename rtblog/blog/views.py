from django.shortcuts import HttpResponse
from django.shortcuts import render

from blog.models import Post
from blog.models import Category


# Create your views here.

def Home(request):
    return  render(request,'index.html', {'title':"rtblog"})

def About(request):
    return render (request,'About.html')

def Services(request):
    return render(request,'Services.html')

def Features(request):
    return render(request,'Features.html')

def Team(request):
    return render(request,'Team.html')

def Blog(request):
    # load all the past from database..
    #ALlData = Post.objects.all()[:11]
    #print(ALlData)
    cats = Category.objects.all()
    posts = Post.objects.all()
    data = {
        'posts':posts,
        'cats':cats
    }
    return render (request,'Blog.html',data)


def ContactUs(request):
    return render (request,'ContactUs.html')

def posts(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    #print (post)
    return render(request,'posts.html',{'post':post,'cats':cats})

def category(request):
    # categories = Category.objects.get(url=url)
    # posters = Post.objects.filter(cat=categories)
    return render (request,'category.html')

