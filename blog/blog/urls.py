from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path('', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()
