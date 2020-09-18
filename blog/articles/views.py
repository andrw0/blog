from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article_list.html', {'articles':articles})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'article_detail.html',{'article':article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        #requested files need the request.FILES, since they dont go with a POST request
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect("article:List")
    else:
        form = forms.CreateArticle()
    return render(request, 'article_create.html', {'form':form})
