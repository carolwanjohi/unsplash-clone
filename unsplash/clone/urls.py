from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url( r'^$', views.index, name="index"),
    url( r'^tag/(\d+)', views.tag, name="tag"),
    url( r'^image-post/(\d+)', views.image_post, name="imagePost"),
    url( r'^search/', views.search_results, name="search_results")
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
    
