# ManageCash - Personal Cash Management System

ManageCash is a Django-based web application developed for tracking personal financial activities. It allows users to manage their income and expenses efficiently while providing an easy-to-use dashboard for monitoring their transactions.

---

## Project Overview

The Personal Cash Management System helps users:

- Track their cash inflow (income).
- Record daily expenses.
- Monitor transaction history.
- Manage their personal financial records.
- View their financial information from a dashboard.

This project was developed using Django as part of the NSDA Level-4 Web Application Development with Python requirements.

---

## Features

### Authentication System

- User Registration
- User Login
- User Logout
- Password Validation
- Profile Management

### Cash Management

Users can:

- Add Cash (Income)
- Add Expenses
- View all transactions
- Update transaction records
- Delete transaction records
- View transaction history

### Dashboard

The dashboard provides:

- Total Cash Added
- Total Expenses
- Current Balance
- User Profile Information
- Financial Overview

---

## Technologies Used

| Technology | Description |
|-----------|------------|
| Python | Programming Language |
| Django | Backend Framework |
| HTML5 | Markup Language |
| CSS3 | Styling |
| Bootstrap | Responsive UI Design |
| SQLite3 | Database |
| Django Authentication | User Management |

---

## Project Structure

```
ManageCash/
│
├── ManageCash_App/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── ManageCash_Project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Database Models

### AddCash Model

| Field Name | Type |
|----------|----------|
| User | ForeignKey |
| Source | CharField |
| Amount | DecimalField |
| Date Time | DateTimeField |
| Description | TextField |

---

### Expense Model

| Field Name | Type |
|----------|----------|
| User | ForeignKey |
| Description | TextField |
| Amount | DecimalField |
| Date Time | DateTimeField |

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/your-username/ManageCash.git
```

Move into the project directory:

```bash
cd ManageCash
```

---

### Create a Virtual Environment

Windows:

```bash
python -m venv env
```

Activate the virtual environment:

```bash
env\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements file, install Django manually:

```bash
pip install django
```

---

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Create Super User

```bash
python manage.py createsuperuser
```

Example:

```
Username: admin
Password: 1234
```

---

### Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## Application Workflow

```
User Registration
        ↓
User Login
        ↓
Profile Dashboard
        ↓
Add Cash
        ↓
Add Expense
        ↓
View Transactions
        ↓
Track Financial Balance
        ↓
Manage Personal Finance
```

---

## Functional Requirements Implemented

- Django Project Creation
- Django Application Creation
- User Authentication System
- Registration Page
- Login Page
- Profile Management
- Cash Management Dashboard
- Add Cash Functionality
- Expense Management Functionality
- Transaction Management
- Database Migration
- Django Admin Configuration
- URL Configuration
- Template Integration

---

## Future Improvements

Some possible future enhancements are:

- Monthly Financial Reports
- Pie Chart for Expenses
- Income vs Expense Analytics
- Search and Filter Transactions
- Export Transaction History as PDF or Excel
- Email Notifications
- Dark Mode Support

---

## Screenshots

You can add screenshots of:

- Login Page
- Registration Page
- Dashboard
- Add Cash Form
- Expense Form
- Profile Page
- Transaction List

---

## Learning Outcomes

Through this project, the following Django concepts were implemented:

- Django Models
- Model Relationships
- Django Forms
- Authentication System
- Template Inheritance
- URL Routing
- CRUD Operations
- Django Admin Panel
- Database Migration
- Static Files Management
- User-Based Data Handling

---

## Author

**Name:** Your Name

**Project:** ManageCash - Personal Cash Management System

**Technology:** Django (Python)

---

## License

This project is developed for educational purposes under the NSDA Level-4 Web Application Development with Python course.
