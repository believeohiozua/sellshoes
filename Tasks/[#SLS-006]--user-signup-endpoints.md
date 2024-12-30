
### User Signup Endpoints
This section outlines the implementation of the signup endpoint, including its logic, response structure, documentation, and testing.

---

### Signup Endpoint

**HTTP Method**: POST  
**URL**: `accounts/signup`

**Request Body Parameters**:
- `email`: The user's email address (must be unique and valid).
- `password`: The user's password (must meet the required strength criteria).
- `first_name`: The user's first name.
- `last_name`: The user's last name.

**Logic**:
1. Validate the provided email to ensure:
   - It is in the correct format.
   - It is not already associated with an existing user.
2. If valid, create a new user with the supplied details.
3. Upon successful signup:
   - Send a welcome email to the user. [example here..](https://www.youtube.com/watch?v=2DM4nI7sCqs)
   - Return a success message with the newly created user's details.
4. If signup fails, return an error message with details about the failure.

**Success Response** (`201 Created`):
```json
{
    "message": "Signup successful",
    "data": {
        "id": 1,
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    "error": null
}
```

**Error Response** (`400 Bad Request`):
```json
{
    "message": "Signup failed",
    "data": null,
    "error": "<error message>"
}
```

---

### API Documentation
Use the `@swagger_auto_schema` decorator from `drf_yasg` to generate API documentation.  
Refer to the following resources for implementation guidance:
- [Swagger Auto Schema Documentation](https://drf-yasg.readthedocs.io/en/stable/custom_spec.html#the-swagger-auto-schema-decorator)
- [Example Video](https://www.youtube.com/watch?v=NVlebOJkzKE)

---

### Test Cases
Write test cases using `pytest` to ensure the functionality of the signup endpoint. Include the following scenarios:

1. **Successful Signup**:
   - Verify that a user can sign up with valid and unique details.

2. **Duplicate Email Signup**:
   - Confirm that the endpoint returns an error when attempting to sign up with an already-registered email address.

3. **Invalid Email**:
   - Ensure that an error is returned for invalid email formats.

---

### References:
- **API Implementation Video**: [Video Example 1](https://www.youtube.com/watch?v=mm6vlnWXFdM)  
- **Swagger Documentation Video**: [Video Example 2](https://www.youtube.com/watch?v=S0S0oxrses8)  
