# hsalpsnU
## This is a clone of [Unspalsh](https://unsplash.com/), a popular photo sharing website, created using Django, 17/11/2017


## By **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
[This](https://django-unsplash-clone.herokuapp.com/) is a web application that is a clone of the popular photo sharing website known as [Unspalsh](https://unsplash.com/). Users can view photographs uploaded by the admin of the site.

## User Stories
As a user I would like:
* to view photos uploaded to the website
* to view photos in a specific tag
* to search for photos by tags
* to see a full image 
* to copy an image link

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display the available tags | N/A | List of tag |
| View photos in a tag | **Click on a tag** | Directed to a page displaying images for the selected tag |
| Display full image | **Click on an image** | Directed to a page displaying the full image |
| Copy an image's link | **Click** copy image link button | Display modal with image url and link for the image |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd unsplash-clone`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE unplsash
```
9. Change the database informatioin in `car/settings.py` 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'unsplash',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
``` 
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application


## Known Bugs

 No known bugs

## Technologies Used
- Python 3.6.2
- Django 1.11.7
- Bootstrap 3
- Postgres Database
- CSS
- HTML
- Heroku

### License

MIT (c) 2017 **[Carol Wanjohi](https://github.com/carolwanjohi)**



