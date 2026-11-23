Student Management System

A Python-based Student Management System integrated with MySQL database connectivity. This project demonstrates database operations, modular programming, and CRUD functionality.

Features

- Add student records
- View all student records
- Search student records
- Update student details
- Delete student records
- MySQL database connectivity
- Modular Python code structure

Technologies Used

- Python
- MySQL
- MySQL Connector
- Git
- GitHub
- VS Code

Project Structure

student-management-system/
│
├── authentication/
│   └── login.py
│
├── database/
│   └── db_connection.py
│
├── students/
│   └── student_operations.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

Installation and Setup

1. Clone the repository
git clone https://github.com/Sharath1106/student-management-system.git

2. Navigate to the project
cd student-management-system

3. Create a virtual environment
python -m venv .venv

4. Activate the environment (Windows)
.venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

6. Configure MySQL

- Start your MySQL server.
- Create the required database and student table.
- Configure your database connection credentials in the database connection module.
- Keep credentials private; do not upload passwords to GitHub.

7. Run the application

python main.py

Concepts Practiced

- Python functions and modules
- Database connectivity
- SQL queries
- CRUD operations
- Exception handling
- Git version control
- GitHub repository management

Future Enhancements

- REST API integration using FastAPI
- API testing using Postman
- Improved input validation
- User authentication enhancements
- Django web interface

Author
Sharath Kumar K S
Python Developer | Python | MySQL | Django | REST APIs