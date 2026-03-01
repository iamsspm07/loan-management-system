# Loan Account Management System

A FastAPI-based web application for managing loan accounts with user authentication, JWT token-based security, and comprehensive CRUD operations.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Error Handling](#error-handling)
- [Project Architecture](#project-architecture)

## ✨ Features

- **User Management**
  - User registration with email validation
  - Secure login with JWT token generation
  - Update user profile information
  - Delete user account with password verification

- **Loan Account Management**
  - Create loan accounts
  - View loan account details
  - Update loan account information
  - Delete loan accounts
  - Automatic loan status tracking

- **Security Features**
  - JWT-based authentication using HS256 algorithm
  - Password hashing with Argon2
  - OAuth2 password bearer token authentication
  - User-specific data isolation

- **Database**
  - PostgreSQL relational database
  - SQLAlchemy ORM for database operations
  - Automatic table creation on startup
  - Foreign key relationships with cascade delete

## 🛠 Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (PyJWT), OAuth2
- **Password Security:** Passlib (Argon2)
- **Data Validation:** Pydantic
- **Database URL Parsing:** urllib.parse

## 📁 Project Structure

```
Loan-Management-System/
│
├── A_DatabasePackage/
│   └── secure_database_connection.py          # Database connection & configuration
│
├── B_EntityPackage/
│   ├── loan_master.py                         # LoanMasterAccount ORM Model
│   └── user_entity.py                         # UserMasterTable ORM Model
│
├── C_SchemaPackage/
│   └── request.py                             # Pydantic schemas for requests
│
├── D_CustomExceptionPackage/
│   └── custom_exception.py                    # Custom exception classes
│
├── E_JWTTokenSecurityPackage/
│   └── jwt_security.py                        # JWT token & security utilities
│
├── F_RepositoryPackage/
│   ├── loan_repository_logic.py               # Loan CRUD operations
│   └── user_repository_logic.py               # User CRUD operations
│
├── G_ServiceFunctionPackage/
│   ├── loan_service_function.py               # Loan service abstract class
│   └── user_service_function.py               # User service abstract class
│
├── H_ServiceImplPackage/
│   ├── loan_service_impl.py                   # Loan service implementation
│   └── user_service_impl.py                   # User service implementation
│
├── I_ControllerPackage/
│   ├── user_controller.py                     # User API endpoints
│   └── loan_controller.py                     # Loan API endpoints
│
└── main.py                                    # FastAPI application entry point
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip or conda package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/loan-management-system.git
cd loan-management-system
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install fastapi sqlalchemy psycopg2-binary pydantic python-jose passlib argon2-cffi python-multipart
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Update the database configuration in `A_DatabasePackage/secure_database_connection.py`:

```python
DB_HOST = "localhost"           # PostgreSQL host
DB_PORT = 5432                  # PostgreSQL port
DB_NAME = "loan_management"     # Database name
DB_USER = "postgres"            # Database user
DB_PASSWORD = "your_password"   # Database password
DB_ECHO = False                 # SQL echo mode (True for debugging)
```

Update JWT configuration in `E_JWTTokenSecurityPackage/jwt_security.py`:

```python
SECRET_KEY = "your-secret-key-here"  # Change to a secure random key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

## 🗄️ Database Setup

### Create PostgreSQL Database
```sql
CREATE DATABASE loan_management;
```

The application will automatically create all tables on startup via `BASE.metadata.create_all(bind=ENGINE)`.

### Database Tables

**user_account Table:**
- `user_id` - Primary Key
- `user_username` - Unique username
- `user_password` - Hashed password
- `user_email` - Unique email address
- `user_created_ts` - Account creation timestamp
- `user_created_date` - Account creation date

**loan_account Table:**
- `loan_id` - Primary Key
- `loan_user_username` - Foreign Key to user_account
- `loan_provider` - Loan provider name
- `loan_account_number` - Unique account number
- `loan_amount` - Loan amount
- `loan_taken_date` - Date loan was taken
- `loan_tenure` - Loan tenure period
- `loan_roi_annual` - Annual ROI percentage
- `loan_emi_amount` - EMI amount
- `loan_emi_date` - EMI payment date
- `loan_disburse_account` - Disbursement account
- `loan_disburse_bank` - Disbursement bank
- `loan_disburse_bank_ifsc` - IFSC code
- `loan_disburse_amount` - Disbursement amount
- `loan_disburse_date` - Disbursement date
- `loan_status` - Loan status (Active, Closed, etc.)

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

Access the application at: `http://localhost:8000`

### Interactive API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔌 API Endpoints

### Authentication Endpoints (`/auth`)

#### Register User
```
POST /auth/register
Content-Type: application/json

{
  "user_username": "john_doe",
  "user_password": "SecurePassword123",
  "user_email": "john@example.com"
}

Response: {
  "Status": "Success",
  "Message": "john_doe Registered Successfully"
}
```

#### Login User
```
POST /auth/login
Content-Type: application/json

{
  "user_username": "john_doe",
  "user_password": "SecurePassword123"
}

Response: {
  "Status": "Success",
  "Message": "Token Created & Login Successful",
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "UserName": "john_doe"
}
```

#### Update User
```
PUT /auth/update
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "user_username": "john_doe",
  "user_password": "NewPassword123"
}

Response: {
  "Status": "Success",
  "Message": "User Updated Successfully",
  "UserName": {...}
}
```

#### Delete User
```
DELETE /auth/delete
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "user_username": "john_doe",
  "user_password": "SecurePassword123"
}

Response: {
  "Status": "Success",
  "Message": "User Deleted Successfully",
  "UserName": "john_doe"
}
```

### Loan Account Endpoints (`/loan`)

#### Create Loan Account
```
POST /loan/create
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "loan_provider": "HDFC Bank",
  "loan_account_number": "LOAN123456",
  "loan_amount": "500000",
  "loan_tenure": "5 Years",
  "loan_roi_annual": "8.5",
  "loan_emi_amount": "9500",
  "loan_emi_date": "2026-03-01",
  "loan_disburse_account": "9876543210",
  "loan_disburse_bank": "HDFC Bank",
  "loan_disburse_bank_ifsc": "HDFC0000001",
  "loan_disburse_amount": "500000",
  "loan_disburse_date": "2026-03-01"
}

Response: {
  "Status": "Success",
  "message": "Loan Account Created",
  "data": {...}
}
```

#### Fetch Loan Accounts
```
GET /loan/get
Authorization: Bearer <access_token>

Response: {
  "Status": "Success",
  "message": "Loan Account List",
  "data": [...]
}
```

#### Update Loan Account
```
PUT /loan/update
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "loan_account_number": "LOAN123456",
  "loan_amount": "550000",
  "loan_roi_annual": "8.75"
}

Response: {
  "Status": "Success",
  "message": "Loan Account Updated",
  "data": {...}
}
```

#### Delete Loan Account
```
DELETE /loan/delete
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "loan_account_number": "LOAN123456"
}

Response: {
  "Status": "Success",
  "message": "Loan Account Deleted",
  "data": {...}
}
```

## 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** with OAuth2 authentication.

### Token Usage
1. Register or login to obtain an access token
2. Include token in request headers:
   ```
   Authorization: Bearer <your_access_token>
   ```
3. Token expires after 30 minutes (configurable)
4. Generate a new token by logging in again

### Token Structure
```
Header: {
  "alg": "HS256",
  "typ": "JWT"
}

Payload: {
  "user_username": "john_doe",
  "exp": 1704067200
}

Signature: HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), SECRET_KEY)
```

## ⚠️ Error Handling

The application uses custom exceptions for consistent error responses:

### NotFoundException
```
Status Code: 404
{
  "detail": "Loan Account Number not found"
}
```

### AlreadyExistsException
```
Status Code: 400
{
  "detail": "User Already Registered"
}
```

### UnauthorizedException
```
Status Code: 401
{
  "detail": "Invalid Username"
}
```

## 🏗️ Project Architecture

The project follows a **layered architecture pattern**:

1. **Controller Layer (I_ControllerPackage)**
   - Handles HTTP requests/responses
   - Routes to appropriate service implementations
   - Applies middleware and dependencies

2. **Service Implementation Layer (H_ServiceImplPackage)**
   - Implements business logic interfaces
   - Coordinates between controllers and repositories
   - Manages transactions and workflow

3. **Service Abstraction Layer (G_ServiceFunctionPackage)**
   - Defines contracts for service implementations
   - Uses abstract base classes for consistency
   - Enables dependency injection

4. **Repository Layer (F_RepositoryPackage)**
   - Contains database CRUD operations
   - Manages entity persistence
   - Handles database queries and transactions

5. **Entity Layer (B_EntityPackage)**
   - SQLAlchemy ORM models
   - Represents database table structures
   - Defines relationships and constraints

6. **Schema Layer (C_SchemaPackage)**
   - Pydantic validation models
   - Request/response schema definitions
   - Data validation and serialization

7. **Security Layer (E_JWTTokenSecurityPackage)**
   - JWT token creation and validation
   - Password hashing and verification
   - OAuth2 authentication middleware

8. **Database Layer (A_DatabasePackage)**
   - Database connection configuration
   - Session management
   - Connection pooling

9. **Exception Layer (D_CustomExceptionPackage)**
   - Custom exception definitions
   - Standardized HTTP error responses

## 📝 Notes

- **Security Important:** Change the `SECRET_KEY` in production to a secure random string
- **Database Password:** Ensure strong passwords for PostgreSQL in production
- **CORS:** Configure CORS settings if accessing from different domains
- **SSL/TLS:** Use HTTPS in production environment
- **Logging:** Implement logging for audit trails and debugging

## 🐛 Known Issues & Future Enhancements

### To-Do Items (from code comments)
- Remove unnecessary fields from database schema:
  - `loan_id`, `loan_taken_date`, `loan_status` from LoanMasterAccount
  - `user_id`, `user_created_ts`, `user_created_date` from UserMasterTable
- Remove updatable fields from update schemas:
  - `user_username`, `user_email` from UserUpdateSchema
  - `loan_account_number` from LoanAccountUpdateSchema

## 📄 License

This project is open source and available under the MIT License.

## 👥 Author
SUJIT SHIBAPRASAD MAITY


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please open an issue on the repository.

---

**Last Updated:** 2026-03-01
