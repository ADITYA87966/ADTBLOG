"""rtblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import Home,About,Services,Features,Team,Blog,ContactUs,posts,category
urlpatterns = [
    path('',Home),
    path('About',About),
    path('Services',Services),
    path('Features',Features),
    path('Team',Team),
    path('Blog',Blog),
    path('ContactUs',ContactUs),
    path('Blog/<slug:url>',posts),
    path('category',category)


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
