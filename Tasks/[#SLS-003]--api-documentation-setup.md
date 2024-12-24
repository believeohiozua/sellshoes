### Open API Documentation Setup

1. **Install the Dependency**  
   Run the following command to install the required package for Swagger API documentation:

   ```bash
   pip install -U drf-yasg
   ```

2. **Add `drf-yasg` to `INSTALLED_APPS`**  
   In your `settings.py` file, add `drf_yasg` to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       # other apps...
       'drf_yasg',
   ]
   ```

3. **Configure `SWAGGER_SETTINGS`**  
   Add the necessary Swagger settings in your `settings.py` file (customize as needed):

   ```python
   SWAGGER_SETTINGS = {
       'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
       # Additional settings can go here if required
   }
   ```

4. **Update `urls.py`**  
   In your `urls.py`, add the following to include Swagger documentation paths:

   ```python
   from drf_yasg.views import get_schema_view
   from drf_yasg import openapi

   schema_view = get_schema_view(
       openapi.Info(
           title="Your API",
           default_version='v1',
           description="API documentation for your project",
           terms_of_service="https://www.google.com/policies/terms/",
           contact=openapi.Contact(email="your-email@example.com"),
       ),
       public=True,
   )

   urlpatterns = [
       # other URL patterns...
       path('test/swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   ]
   ```

   - **Note**: The `path('test/swagger.json')` endpoint is used to test your API's performance.

---

### References:
- **Documentation**: [drf-yasg Documentation](https://drf-yasg.readthedocs.io/en/stable/readme.html#usage)
- **Video Tutorial**: [YouTube Guide](https://www.youtube.com/watch?v=NVlebOJkzKE)

---
