from django.shortcuts import render

def article_list(request):
    return render(request, 'article_list.html')
