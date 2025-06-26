# 🏫 School Management System (Python + MySQL)

A command-line based School Management System that allows users to **sign up**, **log in**, and manage student and teacher records. Built using Python and MySQL.

> ⚠️ Currently designed for **desktop environments**. Mobile-responsive or GUI-based versions may be developed later.

---

## 📌 Features

### 🔐 User Authentication
- Sign Up with username and numeric password
- Log In and verify credentials using MySQL database

### 🎓 Student Module
- Add student details (including personal and academic information)
- Edit specific fields like DOB, phone number, or names
- Delete student records by admission number
- Search students by admission number or name

### 👨‍🏫 Teacher Module
- Add teacher details (including qualification and date of joining)
- Edit fields like phone number, qualification, gender etc.
- Delete teacher records by ID
- Search teachers by ID or name

---

## 🛠️ Technologies Used

- **Python** – for program logic and CLI interaction
- **MySQL** – for data storage and retrieval
- **MySQL Connector** – for connecting Python with MySQL

---

## ⚙️ Setup Instructions

1. Install required MySQL connector:
   ```bash
   pip install mysql-connector-python
