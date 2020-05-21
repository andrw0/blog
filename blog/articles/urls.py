from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.article_list, name='List'),
    path("<slug:slug>/", views.article_detail, name='detail')
]
