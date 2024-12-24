---

### Email Configuration Setup

1. **Create an Experimental Gmail Account:**
   - Create a Gmail account or use an existing one for experimental purposes.
   - Generate an app password by following the guide in the [Refs section below].

2. **Add Configuration to `settings.py`:**

   In your `settings.py` file, add the following email configuration:

   ```python
   EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
   EMAIL_HOST = "smtp.gmail.com"
   EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="your-email@gmail.com", cast=str)  # Your Gmail address
   SERVER_EMAIL = EMAIL_HOST_USER
   EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="your-app-password", cast=str)  # App password
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_USE_SSL = False
   ```

   _Make sure to add `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to your `.env` file in the project directory (`sellshoes/`)._

3. **Add to `.env` File:**

   In your `.env` file, add the following:

   ```bash
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

---

### References:
- **Generate App Password**: [Enable Google App Passwords for SMTP](https://www.febooti.com/products/automation-workshop/tutorials/enable-google-app-passwords-for-smtp.html)
- **Video Tutorial**: [YouTube Guide](https://www.youtube.com/watch?v=74QQfPrk4vE)

---
