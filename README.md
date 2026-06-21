# GenAIDay6-Buildathon

📅 Leave Management System
Overview
The Leave Management System is a web-based application that enables employees to apply for leave and managers to review, approve, or reject leave requests.
The system provides:
•	Employee registration and login 
•	Role-based access control 
•	Leave application management 
•	Manager approval workflow 
•	Leave history tracking 
•	SQLite database integration 
•	Streamlit user interface 
•	FastAPI backend APIs 
________________________________________
Features
Employee Features
•	User Registration 
•	Secure Login 
•	Apply for Leave 
•	View Leave Status 
•	View Leave History 
•	Logout 
Manager Features
•	Login as Manager 
•	View All Leave Requests 
•	Approve Leave Requests 
•	Reject Leave Requests 
•	Monitor Employee Leave Records 
________________________________________
Technology Stack
Component	Technology
Frontend	Streamlit
Backend API	FastAPI
Database	SQLite
Authentication	Custom Python Authentication
Styling	CSS
Language	Python 3.x
________________________________________
Project Structure
leave-management-system/
│
├── app.py
├── main.py
├── database.py
├── auth.py
├── leave_management.db
│
├── pages/
│   ├── employee.py
│   └── manager.py
│
├── assets/
│   └── style.css
│
└── README.md
________________________________________
Database Schema
Leave Requests Table
CREATE TABLE leave_requests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    leave_type TEXT,
    start_date TEXT,
    end_date TEXT,
    reason TEXT,
    status TEXT
);
Status Values
Pending
Approved
Rejected
________________________________________
Installation
Clone Repository
git clone https://github.com/yourusername/leave-management-system.git

cd leave-management-system
Create Virtual Environment
Windows
python -m venv venv

venv\Scripts\activate
Linux/Mac
python3 -m venv venv

source venv/bin/activate
Install Dependencies
pip install streamlit
pip install fastapi
pip install uvicorn
pip install pydantic
Or
pip install -r requirements.txt
________________________________________
Running Streamlit Application
streamlit run app.py
Application URL:
http://localhost:8501
________________________________________
Running FastAPI Backend
uvicorn main:app --reload
API URL:
http://localhost:8000
Swagger Documentation:
http://localhost:8000/docs
________________________________________
API Endpoints
Apply Leave
POST
/api/apply-leave
Request
{
  "employee_name": "John",
  "leave_type": "Casual Leave",
  "start_date": "2026-06-20",
  "end_date": "2026-06-22",
  "reason": "Personal Work"
}
Response
{
  "message": "Leave Applied"
}
________________________________________
View Leave History
GET
/api/leave-history
Response
[
  {
    "id": 1,
    "employee_name": "John",
    "leave_type": "Casual Leave",
    "start_date": "2026-06-20",
    "end_date": "2026-06-22",
    "reason": "Personal Work",
    "status": "Pending"
  }
]
________________________________________
Approve Leave
PUT
/api/approve/{leave_id}
Example
PUT /approve/1
Response
{
  "message": "Approved"
}
________________________________________
Reject Leave
PUT
/api/reject/{leave_id}
Example
PUT /reject/1
Response
{
  "message": "Rejected"
}
________________________________________
User Roles
Employee
Can:
•	Register 
•	Login 
•	Apply Leave 
•	View Own Leave Requests 
Cannot:
•	Approve Leave 
•	Reject Leave 
Manager
Can:
•	Login 
•	View All Leave Requests 
•	Approve Leave 
•	Reject Leave 
________________________________________
Workflow
Employee
    |
    v
Apply Leave
    |
    v
Status = Pending
    |
    v
Manager Reviews Request
    |
    +----> Approve
    |          |
    |          v
    |     Status = Approved
    |
    +----> Reject
               |
               v
        Status = Rejected
________________________________________
Future Enhancements
•	Password Hashing (bcrypt) 
•	Email Notifications 
•	Leave Balance Management 
•	Multi-Level Approvals 
•	HR Dashboard 
•	Audit Logs 
•	Calendar Integration 
•	Employee Profile Management 
•	Department Management 
•	Role-Based Permissions 
•	Docker Deployment 
•	Cloud Deployment (Azure/AWS) 
________________________________________
Author
Senthilkumar Sivasankaran
Python | Streamlit | FastAPI | SQLite
________________________________________
Current Limitations
1.	Passwords appear to be stored without encryption. 
2.	SQLite is suitable for development but not large-scale production. 
3.	No leave balance validation. 
4.	No date validation. 
5.	No email notification mechanism. 
6.	No JWT/session security for API endpoints. 
7.	Duplicate code exists in app.py and manager.py and can be refactored. 
________________________________________
Suggested Resume Project Description
Leave Management System | Python, Streamlit, FastAPI, SQLite
Developed a role-based Leave Management System enabling employees to submit leave requests and managers to approve or reject requests. Implemented authentication, leave workflow automation, SQLite database integration, REST APIs using FastAPI, and an interactive Streamlit user interface for efficient leave tracking and management.

