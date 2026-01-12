# 🔐 Identity & Access Management (IAM) System

An enterprise-style **Identity & Access Management (IAM)** web application built using **Flask and MySQL**, implementing **Role-Based Access Control (RBAC)**, permission matrices, and secure session handling.

This project closely aligns with **Deloitte IAM / SOC / GRC simulations** and demonstrates real-world access governance concepts used in large organizations.

---

## 🚀 Key Features

- ✅ User authentication (login & logout)
- ✅ Role-Based Access Control (RBAC)
- ✅ Permission matrix per role
- ✅ Session-based access enforcement
- ✅ Admin-only protected routes
- ✅ Enterprise-style IAM dashboard UI
- ✅ Separation of authentication & authorization logic

---

## 🛠️ Tech Stack

- **Backend:** Python  
- **Framework:** Flask  
- **Database:** MySQL  
- **Authentication:** Session-based  
- **Access Control:** RBAC (Role-Based Access Control)  
- **Frontend:** HTML + CSS (Enterprise dark UI)

---

## 🧠 Cybersecurity & IAM Concepts Covered

- Identity & Access Management (IAM)
- Authentication vs Authorization
- Role-Based Access Control (RBAC)
- Permission matrix design
- Least privilege principle
- Session management
- Admin privilege segregation
- Access governance fundamentals

> ⚠️ This project is for **educational and demonstration purposes**.  
> In production, password hashing (bcrypt), MFA, and audit logging should be used.

---


## ⚙️ Database Schema Overview

### Users Table
| Field | Description |
|-----|-------------|
| id | Unique user ID |
| username | Login identity |
| password | User password |
| role | Assigned role |

### Permissions Table
| Field | Description |
|-----|-------------|
| role | Role name |
| permission | Allowed action |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/iam_system.git
cd iam_system
2️⃣ Install Dependencies
python -m pip install -r requirements.txt

3️⃣ Setup MySQL Database
Login to MySQL and run:
SOURCE schema.sql;
Update database credentials in db.py:

host="localhost"
user="root"
password="YOUR_PASSWORD"
database="iam_db"


4️⃣ Run the Application
python app.py
Open in browser:
http://127.0.0.1:5000

👤 Demo Accounts
Username	Password	Role
admin	admin123	ADMIN
analyst	analyst123	ANALYST

🔐 Access Control Logic
Role	Permissions
ADMIN	VIEW_DASHBOARD, MANAGE_USERS
ANALYST	VIEW_DASHBOARD

Admin users can access the Admin Control Panel

Analysts are restricted to dashboard-only access

Unauthorized access attempts return 403 Forbidden

🖥️ Application Flow
User logs in

System authenticates credentials

Role and permissions loaded into session

Access is enforced at route level

UI adapts based on assigned permissions

Admin-only routes are protected


🔮 Future Enhancements
bcrypt password hashing

Multi-Factor Authentication (MFA)

Audit logs & access reviews

User provisioning & deprovisioning

Role hierarchy

JWT-based authentication

IAM + SIEM integration

👨‍💻 Author
Sarthak Santosh Dhatrak
Cybersecurity & Blockchain Enthusiast
IAM • SOC • Secure Web Systems

📜 License
This project is licensed for educational and non-commercial use.
Unauthorized or malicious usage is prohibited.
