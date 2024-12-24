---

### Cloudinary Media Storage Setup

1. **Install Cloudinary Dependency**  
   First, install the required `django-cloudinary-storage` package using pip:

   ```bash
   pip install django-cloudinary-storage
   ```

2. **Add to `INSTALLED_APPS`**  
   In your `settings.py` file, add `cloudinary` and `cloudinary_storage` to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       # other apps...
       'cloudinary',
       'cloudinary_storage',
   ]
   ```

3. **Configure Cloudinary in `settings.py`**  
   Add the Cloudinary credentials and media storage configuration to your `settings.py` file. You'll need to get your `CLOUDINARY_URL` from your Cloudinary dashboard.

   ```python
   import cloudinary
   import cloudinary.uploader
   import cloudinary.api

   CLOUDINARY_STORAGE = {
       'CLOUD_NAME': 'your-cloud-name',  # Replace with your Cloudinary cloud name
       'API_KEY': 'your-api-key',        # Replace with your Cloudinary API key
       'API_SECRET': 'your-api-secret',  # Replace with your Cloudinary API secret
   }

   DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   ```

4. **Configure Media URL**  
   Ensure that the `MEDIA_URL` is set to Cloudinary's URL in your `settings.py`:

   ```python
   MEDIA_URL = '/media/'
   ```

5. **Uploading Media Files**  
   Now, when you upload files in your Django app (such as images), Cloudinary will handle the storage automatically.

6. **Optional: Custom Cloudinary Storage Settings**  
   You can specify additional options for Cloudinary media uploads (e.g., transformations, format settings) in your `settings.py` file.

   Example for defining specific storage settings:

   ```python
   CLOUDINARY_STORAGE = {
       'CLOUD_NAME': 'your-cloud-name',
       'API_KEY': 'your-api-key',
       'API_SECRET': 'your-api-secret',
       'SECURE': True,  # Use HTTPS URLs
       'CACHE_PREVIOUS_VERSIONS': True,  # Cache previous versions of media files
   }
   ```

---

### References:
- **Documentation**: [Managing Media Files in Django](https://cloudinary.com/blog/managing-media-files-in-django)

---
