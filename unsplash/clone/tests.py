from django.test import TestCase
from .models import User, tags

# Create your tests here.
class UserTestClass(TestCase):
    '''
    Test case for User class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a User instance before each test
        '''
        # Create a user instance
        self.new_user = User(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    def test_instance(self):
        '''
        Test case to check if self.new_user in an instance of User class
        '''
        self.assertTrue( isinstance(self.new_user, User) )

    def test_save_user(self):
        '''
        Test case to check is a user is saved in the database
        '''
        self.new_user.save_user()
        users = User.objects.all()
        self.assertTrue( len(users) > 0 )

    def test_delete_user(self):
        '''
        Test case to check if a user is deleted from the database
        '''
        self.new_user.save_user()
        users = User.objects.all()
        self.new_user.delete_user()
        self.assertTrue( len(users) == 0)

    def test_get_users(self):
        '''
        Test case to check if all users are gotten from the database
        '''
        self.new_user.save_user()
        gotten_users = User.get_users()
        users = User.objects.all()
        self.assertTrue( len(gotten_users) == len(users))

class tagsTestClass(TestCase):
    '''
    Test case for tags class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a tags instance before each test
        '''
        self.new_tag = tags(name='Python')

    def test_instance(self):
        '''
        Test case to check if self.new_tag in an instance of tags class
        '''
        self.assertTrue( isinstance(self.new_tag, tags) )

    def test_save_editor(self):
        '''
        Test case to check is a tag is saved in the database
        '''
        self.new_tag.save_tag()
        gotten_tags = tags.objects.all()
        self.assertTrue( len(gotten_tags) > 0 )

    def test_delete_tag(self):
        '''
        Test case to check if a tag is deleted from the database
        '''
        self.new_tag.save_tag()
        gotten_tags = tags.objects.all()
        self.new_tag.delete_tag()
        self.assertTrue( len(gotten_tags) == 0 )

    def test_get_tags(self):
        '''
        Test case to check if all tags are gotten from the database
        '''
        self.new_tag.save_tag()
        gotten_tags = tags.get_tags()
        existing_tags = tags.objects.all()
        self.assertTrue( len(gotten_tags) == len(existing_tags))

    def test_search_by_tag(self):
        '''
        Test case to check if tags containg a search term is gotten from the database 
        '''
        self.new_tag.save_tag()
        found_tags = tags.search_by_tag('Python')
        self.assertTrue( len(found_tags) == 1)




