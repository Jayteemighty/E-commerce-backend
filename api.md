# API DOCUMENTATION

## Ecommerce Backend

This project contains APIs for an Ecommerce website. It includes logic(django apps) such as Accounts, Order, Product. while the django project named backend contains configuration of settings and urls.

BASE_URL = https://e-commerce-backend-fe1r.onrender.com/ or http://127.0.0.1:8000/ depending on whether you are using the deployed api or you cloned the repository

### 1. Authentication:

#### POST /api/signup
 
 Description: Creates a new user account.

 Request Body:

   ```bash
   {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
 }


Response:
Status: 201 Created
Body:
    ```bash
    {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
    }
