from django.shortcuts import render,redirect
from .models import Post,Category
from .forms import VisitorForm
import random

def index(request):
    
    featuredPost = Post.objects.filter(featured=True)
    index = randnum()
    allCategories = Category.objects.all()
    categorisedPost = Post.objects.filter(category=allCategories[index])
    
    if request.method == "POST":
            form = VisitorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

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

    if request.GET.get('article'):
        catTitle = request.GET.get('article')
        featuredPost = Post.objects.filter(pk=catTitle)
    if request.GET.get('catpk'):
        if str(request.GET.get('catpk'))[0] == "0":
            catTitle = str(request.GET.get('catpk')).strip(str(request.GET.get('catpk'))[0])
            catTitle = str(int(catTitle)+1)
        else : catTitle = request.GET.get('catpk')
        featuredPost = Post.objects.filter(category=catTitle)
        

    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else :
        form = VisitorForm()
    context = {
        'form':form,
        'post_list': featuredPost,
        'cat_list': allCategories,
        'catpost_list':categorisedPost

    }
    return render(request,'blog.html',context)