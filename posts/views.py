from django.shortcuts import render 
from .models import Post,Category
import random

def index(request):
    featuredPost = Post.objects.filter(featured=True)
    index = randnum()
    allCategories = Category.objects.all()
    categorisedPost = Post.objects.filter(category=allCategories[index])
    context = {
        'post_list': featuredPost,
        'cat_list': allCategories,
        'catpost_list':categorisedPost

    }
    return render(request,'index.html',context)

def randnum():
    return random.randint(0,2)
 
def blog(request):
    featuredPost = Post.objects.filter(featured=True)
    index = randnum()
    allCategories = Category.objects.all()
    categorisedPost = Post.objects.filter(category=allCategories[index])
    context = {
        'post_list': featuredPost,
        'cat_list': allCategories,
        'catpost_list':categorisedPost

    }
    return render(request,'blog.html',context)