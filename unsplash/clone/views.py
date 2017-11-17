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

def tag(request,tag_id):
    '''
    View function to display images in a single tag
    '''
    try:
        tag = tags.objects.get(id=tag_id)
    except DoesNotExist:
        raise Http404()

    title = f'{tag.name} phots'
    return render(request, 'all-posts/tag.html', {"title":title, "tag":tag})


