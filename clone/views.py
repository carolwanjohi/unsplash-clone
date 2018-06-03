from django.shortcuts import render, redirect
from django.http import Http404
from .models import tags, ImagePost

# API Practice
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ImagePostSerializer
from .permissions import IsAdminOrReadOnly

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

def image_post(request,image_post_id):
    '''
    View function to display an image in full
    '''
    try:
        image_post = ImagePost.objects.get(id=image_post_id)
    except DoesNotExist:
        raise Http404()
    title = f'{image_post.name}'
    return render(request, 'all-posts/image-post.html', {"title":title, "image_post":image_post})

def search_results(request):
    '''
    View function to display search results
    '''
    if 'tag' in request.GET and request.GET['tag']:
        search_term = request.GET.get('tag')
        searched_tags = tags.search_by_tag(search_term)
        try:
            single_tag = searched_tags[0]
            image_posts = ImagePost.objects.filter(tags=single_tag).all()

        except IndexError:

            message = f'{search_term}'
            return render(request, 'all-posts/search.html', {"message":message})
            
        message = f'{search_term}'
        title = f'{search_term}'
        return render(request, 'all-posts/search.html', {"title": title, "message":message, "image_posts":image_posts, "tags":searched_tags})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html', {"message":message})

def collections(request):
    '''
    View function to display all the tags available
    '''
    gotten_tags = tags.get_tags()
    title = 'Collections'
    return render(request,'all-posts/collections.html', {"tags":gotten_tags})

class ImagePostList(APIView):
    '''
    API View to handle requests
    '''
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        '''
        Get method that queries the database and gets all the ImagePost instances in the database 
        '''
        all_image_post = ImagePost.objects.all()
        serializers = ImagePostSerializer(all_image_post, many=True)
        return Response(serializers.data)

