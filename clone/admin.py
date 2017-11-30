from django.contrib import admin
from .models import User, tags, ImagePost

class ImagePostAdmin(admin.ModelAdmin):
    '''
    Customise model in admin page
    '''
    filter_horizontal = ('tags',)

# Register your models here.
    
admin.site.register(User)
admin.site.register(ImagePost,ImagePostAdmin)
admin.site.register(tags)


