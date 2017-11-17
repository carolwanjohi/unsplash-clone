from django.db import models

# Create your models here.
class User(models.Model):
    '''
    Class that defines a User for the application
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_user(self):
        '''
        Method to save a new User to the database
        '''
        self.save()

    def delete_user(self):
        '''
        Method to delete a User from the database
        '''
        self.delete()

    @classmethod
    def get_users(cls):
        '''
        Method that gets all users from the database

        Returns:
            users : list of user objects from the database
        '''
        users = User.objects.all()
        return users

class tags(models.Model):
    '''
    Class that defines categories of photographs and tags on image posts
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tag(self):
        '''
        Method to save a new tag to the database
        '''
        self.save()

    def delete_tag(self):
        '''
        Method to delete a tag from the database
        '''
        self.delete()

    @classmethod
    def get_tags(cls):
        '''
        Method that gets all tags from the database

        Returns:
            gotten_tags : list of tag objects from the database
        '''
        gotten_tags = tags.objects.all()
        return gotten_tags

    @classmethod
    def search_by_tag(cls,search_term):
        '''
        Method that gets tags matching the specific search term

        Args:
            search_term : specific tag name from the user

        Returns
            tags : list of tags objects from the database matching the specific search term
        '''
        tags = cls.objects.filter(name__icontains=search_term)
        return tags




