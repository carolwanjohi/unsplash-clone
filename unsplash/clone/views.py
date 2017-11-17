from django.shortcuts import render, redirect
from django.http import Http404
from .models import tags, ImagePost

# Create your views here.
def index(request):
    '''
    View function that returns a list of tags and images on the home page
    '''
    gotten_tags = tags.get_tags()
    title = 'hsalpsnU Home'
    return render(request, 'all-posts/index.html', {"title":title, "tags":gotten_tags})

