##### Title: Create User Account Setup

Decsription: Create a user account for the web application.
- clone the application from the repository
- create a virtual environment and activate your virtual environment
- get into the sellshoes project directory `cd sellshoes`
- install the requirements.txt file `pip install -r requirements.txt`
- create a new django app called account `python manage.py startapp accounts` 
  - do not forget to add the app to the installed apps in the _settings.py_ file
- create a custom user model see by abstracting and extending Baseusermanager and AbstractBaseUser see #Refs below for more details
- add the custom user model to the _settings.py_ file
- make migrations and migrate into the database
- create the admin interface for the custom user model in the _admin.py_ file


```bash
NOTE: 
- All the  tasks above must be done and approved before moving to the Next.
- With the above tasks donbe we can then finish project setup configuration and move to the next task.
```



##### Refs
blog-post: 
- https://medium.com/@iamalisaleh/creating-a-custom-user-model-in-django-step-by-step-guide-f493ac5f28e4
- https://testdriven.io/blog/django-custom-user-model/

video: 
- https://www.youtube.com/watch?v=NpJKB2b5fl0