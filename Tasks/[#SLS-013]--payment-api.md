#### Payments API

The goal of this task is to create an API that enables users to make payments using their bank card. The API should rely on the Stripe payment gateway to handle the payment process securely.  

**Key Objectives:**

1. **Do Not Store Sensitive Information:**  
   - Users' payment details (e.g., card information) must not be stored in the database.  

2. **Core API Functionalities:**  
   - Accept card details and the amount to be paid.  
   - Process the payment using the provided card details via the Stripe payment gateway.  
   - Return appropriate responses:
     - **Success Message:** When the payment is successful.  
     - **Error Message:** When the payment fails.  

3. **Integration with User Profile:**  
   - Save the success or error message to the user's market profile.  
   - Update or adjust the **BankCard/Payment model** to reflect this requirement.  

---

### Resources to Get Started

Here are some helpful reads to guide you through the integration process:  

- [How to integrate Stripe Payment Gateway in Django Rest Framework](https://medium.com/@hari154542/how-to-integrate-stripe-payment-gateway-in-django-rest-framework-232ee341601)  
- [Stripe API Documentation](https://docs.stripe.com/api?lang=python)  

--- 