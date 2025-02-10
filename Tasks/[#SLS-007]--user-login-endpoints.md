### Login Endpoint

**HTTP Method**: POST  
**URL**: `accounts/login`

**Request Body Parameters**:
- `email`: The user's email address (must be registered and valid).
- `password`: The user's password (must match the stored password for the user).

**Logic**:
1. Validate the provided email to ensure:
   - It exists in the system.
   - It is in the correct format.
2. If valid, decrypt the stored password and compare it with the provided password.
3. If authentication is successful:
   - Return a success message with a JWT token for session management.
4. If authentication fails:
   - Return an error message detailing the failure, such as incorrect credentials.

**Success Response** (`200 OK`):
```json
{
    "message": "Login successful",
    "data": {
        "access_token": "<JWT token>"
    },
    "error": null
}
```

**Error Response** (`400 Bad Request`):
```json
{
    "message": "Login failed",
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
Write test cases using `pytest` to ensure the functionality of the login endpoint. Include the following scenarios:

1. **Successful Login**:
   - Verify that a user can log in with the correct email and password, and receive a valid JWT token.

2. **Invalid Email**:
   - Ensure that an error is returned for emails that are not registered in the system.

3. **Incorrect Password**:
   - Confirm that the endpoint returns an error when the provided password does not match the stored password.

4. **Missing Credentials**:
   - Test that the API returns an error if either the email or password is missing from the request.

---

### References:
- **API Implementation Video**:  --
- **Swagger Documentation Video**: --