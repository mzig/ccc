"""ccc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from nucleo.admin import admin_site
# from eventos.admin import admin_site

# static for debug mode
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views


# from nucleo.views import HomePageView
from django.views.generic.base import TemplateView
from nucleo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),

    # url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^expos/$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='expo'),


    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^exposiciones/$', views.ExpoListView.as_view(), name='exposiciones'),
    url(r'^exposiciones/(?P<slug>[-\w]+)/$', views.ExpoDetailView.as_view(), name='exposicion'),
    url(r'^exposiciones/archivo$', views.ArchivoExposListView.as_view(), name='archivo'),
    url(r'^actividades/$', views.ActsListView.as_view(), name='actividades'),
    url(r'^actividades/(?P<slug>[-\w]+)/$', views.ActsDetailView.as_view(), name='actividad'),
    url(r'^actividades/archivo$', views.ArchivoActsListView.as_view(), name='archivo_de_actividades'),
    url(r'^publicaciones/$', views.PublsListView.as_view(), name='publicaciones'),
    #
    url(r'^(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='articulo'),
    # url(r'^acercade/$', views.ArticleView.as_view(), name='acercade'),
    # url(r'^contacto/$', views.ArticleView.as_view(), name='contacto'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)