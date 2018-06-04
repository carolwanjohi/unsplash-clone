# hsalpsnU
#### This is a clone of [Unspalsh](https://unsplash.com/), a popular photo sharing website, created using Django, 17/11/2017


#### By **[Carol Wanjohi](https://github.com/carolwanjohi)**

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
```
git clone https://github.com/carolwanjohi/unsplash-clone.git && cd cd unsplash-clone
virtualenv virtual or python3.6 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
```
* Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
USER=<your postgresql username>
PASSWORD=<your postgresql password>
```
* Create Postgres Database
```
psql
CREATE DATABASE unsplash;
```
### Running the application
```
./manage.py runserver or python3.6 manage.py runserver
```

### Running the tests
```
./manage.py test or python3.6 manage.py test
```

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



