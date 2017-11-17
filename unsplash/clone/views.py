from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.
def index(request):
    '''
    View function that returns a list of tags and images on the home page
    '''
    message = "Home page"
    title = 'hsalpsnU Home'
    return render(request, 'all-posts/index.html', {"message":message, "title":title})

