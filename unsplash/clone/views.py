from django.shortcuts import render, redirect
from django.http import Http404
from .models import tags, ImagePost

# Create your views here.
def index(request):
    '''
    View function that returns a list of tags and images on the home page
    '''
    gotten_tags = tags.get_tags()
    image_posts = ImagePost.get_image_posts()
    title = 'hsalpsnU Home'
    return render(request, 'all-posts/index.html', {"title":title, "tags":gotten_tags, "image_posts":image_posts})

def tag(request,tag_id):
    '''
    View function to display images in a single tag
    '''
    try:
        tag = tags.objects.get(id=tag_id)
        image_posts = ImagePost.objects.filter(tags=tag).all()
    except DoesNotExist:
        raise Http404()

    title = f'{tag.name} phots'
    return render(request, 'all-posts/tag.html', {"title":title, "tag":tag, "image_posts":image_posts})


