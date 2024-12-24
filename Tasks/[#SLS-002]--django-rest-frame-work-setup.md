##### Django Rest Framework setup
- Follow the links in the #Ref section to create a setup for the Django Rest Framework
- install the dependency `pip install djangorestframework`
- add the app to the `INSTALLED_APPS` in the `settings.py` file
- no need to add configurations the `urls.py` file since we are going to so this with swagger.
- add the configurations to the `settings.py` file

```python
`REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
``` 




#### Ref
- Videos:
    - https://www.youtube.com/watch?v=263xt_4mBNc
    - https://www.youtube.com/watch?v=Uyei2iDA4Hs

- Links:
    - https://www.django-rest-framework.org/