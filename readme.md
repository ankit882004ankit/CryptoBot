# CryptoBot

CryptoBot is a Django-based web application designed to manage cryptocurrency alerts and user authentication using Django Rest Framework and JWT for secure token-based authentication.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Features

- **User Registration and Authentication:**
  - Register new users and manage authentication with JWT tokens.
- **Create and Manage Alerts:**
  - Create, list, and delete cryptocurrency alerts.
- **API Documentation:**
  - Swagger and ReDoc for API documentation.
- **Admin Panel:**
  - Manage users and alerts through Django's built-in admin interface.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cryptobot.git
   cd cryptobot
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the required package for JWT authentication:**

   ```bash
   pip install djangorestframework-simplejwt
   ```

5. **Add SimpleJWT to your Django project:**

   Add the following in `settings.py`:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }
   ```

6. **Setup your PostgreSQL Database:**

   Ensure that you have PostgreSQL installed. You can follow the instructions [here](https://www.postgresql.org/download/).

   - **Create a Database:**

     ```bash
     psql -U postgres
     CREATE DATABASE cryptobot;
     ```

   - **Add Database Credentials:**

     Edit `settings.py` to reflect your PostgreSQL database details:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'cryptobot',
             'USER': 'your_postgres_username',
             'PASSWORD': 'your_postgres_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

## Setup

1. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin account.

3. **Start the Development Server:**

   ```bash
   python manage.py runserver
   ```

4. **Access the Admin Panel:**

   Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to log in with the admin credentials you just created.

## Usage

### API Endpoints

Here are some of the key endpoints for interacting with the CryptoBot API:

#### User Authentication

- **Register:** `POST /alerts/register/`

  Request Body:

  ```json
  {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "password": "securepassword123"
  }
  ```

- **Login:** `POST /api/token/`

  Request Body:

  ```json
  {
    "username": "john_doe",
    "password": "securepassword123"
  }
  ```

  Response:

  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

- **Logout:** `POST /alerts/logout/`

  Request Body:

  ```json
  {
    "refresh": "<refresh_token>"
  }
  ```

- **Refresh Token:** `POST /api/token/refresh/`

  Request Body:

  ```json
  {
    "refresh": "<refresh_token>"
  }
  ```

#### Alerts

- **Create Alert:** `POST /alerts/create/`

  Request Body:

  ```json
  {
    "currency": "BTC",
    "price_threshold": "30000"
  }
  ```

- **List Alerts:** `GET /alerts/`

- **Delete Alert:** `DELETE /alerts/delete/<alert_id>/`

### Running the Server

```bash
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Documentation

The CryptoBot API is documented using Swagger and ReDoc. You can access the documentation via the following endpoints:

- **Swagger:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **ReDoc:** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)
