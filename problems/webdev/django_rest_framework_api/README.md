# Build an API with Django REST Framework

## Overview 
For this project, we will be creating a functioning REST API. REST APIs can help distribute useful information via GET requests, as well as post and alter databases in a user friendly fashion.

This project will revolve around using Django and Django's REST framework to build an API for the dataset of your choice. Django is a full web framework capable of handling both back and front end portions of a web app; and the Django team has created great resources to make setting up a Django app quick and easy.

While the project is structured around Django, feel free to use flask instead, if you're more comfortable.

## Environment Setup
To avoid bloating of your primary working environment, we strongly recommend creating a virtual environment. The requirements.txt file includes the required packages, and the included versions have been tested for our needs - use different versions at your own risk.

We also strong recommend using [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/3) as your text editor. This project has also NOT been tested using Jupyter Notebook, PyCharm,
Spider, or any other ide/text editor/programming environment.

1. For this challenge you will need Python 3.7, pipenv, and git installed. If you're not familiar with pipenv, it's a packaing tool for Python that effectively replaced the pip+virtualenv+requirements.txt workflow. If you already have pip installed, the easiest way to install pipenv is with `pip install --user pipenv`; however, a better way for Mac/Linux Homebrew users is to instead run `brew install pipenv`. More options can be found [here](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv).

2. The project is in the ChiPy project night repo. If you do not have the repository already, run 

	```
	git clone https://github.com/chicagopython/CodingWorkshops.git
	```

3. Navigate to the folder for this challenge:

	```
	cd CodingWorkshops/problems/webdev/django_rest_framework_api
	```

4. Run `pipenv install`, which will install all of the libraries we have recommended for this exercise.
5. After you've installed all of the libraries, run `pipenv shell`, which will turn on a virtual environment running Python 3.7.
6. To exit the pipenv shell when you are done, simply type `exit`.

## Instructions

### Find a Database
- Before advancing, find a database that you wish to use for a REST API. It helps if the data is something you are interested in, but don't waste too much time on this part. [Kaggle](https://www.kaggle.com/tags/databases) has a great selection of publicly available databases. If you are looking for something specific, Google has a stellar [database search](https://toolbox.google.com/datasetsearch) feature.

### Create Your First App

- Create a Django app in a local directory of your choosing. Feel free to use the [Django tutorial]((https://docs.djangoproject.com/en/2.2/intro/tutorial01/)) to accomplish this, but please don't call your app the standard Polls App. Create a unique application inside of your Django directory to handle your database and models. Make sure the application is configured in your settings.py file!

### Create a Django Model
- Create a Django model custom to your database. Feel free to take liberties like creating relational databases for your models. The model field types should match the intended fields of your database. Make sure to migrate your Django model when you are finished!

### Configure the REST framework
- Make sure you appropriately configure Django REST Framework in your settings.py file. If you forget this step, Django to recognize the add on.

### Serialization
- Before creating a url or view, serialize your data. This allows Django to render data into a JSON format. Make sure you designate the table (model) and fields (features) you wish to include in your REST API.

### Create a View
- Use the standard Django REST framework to create your Django view. Django REST framework allows you to interact with your API in both JSON and a preset interactive template. If you feel like going the extra mile, make your database queryable to gather the information you need.

### Designating a URL
- Finally, designate url addresses where your page views can be found. Make sure to create a URL scheme that makes sense to how the intended user will interact with your API.

### Running your Server
- At this point it is time to test your API. This can be accomplished by the manage.py runserver command. Django's default location is localhost:8000/. From there, follow the naming scheme you created in your urls. Feel free to play with your API by using those filterable features you created!


## Useful Weblinks


- Django Startup and Features

	https://docs.djangoproject.com/en/2.2/intro/tutorial01/

	https://docs.djangoproject.com/en/2.2/ref/applications/

- Django Models

	https://docs.djangoproject.com/en/2.2/ref/models/fields/

	https://docs.djangoproject.com/en/2.2/topics/db/models/#automatic-primary-key-fields

- Django REST Framework

	https://www.django-rest-framework.org/#installation

- Serialization

	https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

	https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields

- Views and URLS

	https://www.django-rest-framework.org/tutorial/quickstart/#views

	https://www.django-rest-framework.org/tutorial/quickstart/#urls