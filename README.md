
# Collection_Manipulation_-Student_Management-_project
Collection Manipulation Student Management project
<div align="center">

# 🎓 Student Data Organizer

### Simple Python-Based Student Management System

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=28&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Student+Data+Organizer;Manage+Student+Records;Add+%7C+Display+%7C+Update+%7C+Delete;Python+%7C+Lists+%7C+Dictionaries+%7C+Sets;Built+with+Python" alt="Animated Typing Header"/>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-111827?style=for-the-badge)
![Data Management](https://img.shields.io/badge/Data-Management-00C2FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

</div>

---

# 🌟 About The Project

**Student Data Organizer** is a simple Python-based command-line application designed to manage student information.

The program allows users to add student records, display all students, update student information, delete students, and display the subjects associated with students.

This project focuses on practising core Python concepts such as **lists, dictionaries, sets, loops, conditional statements, functions through program structure, and user input handling**.

> **"Organize student data with simple and practical Python."**

---

# 🎯 Project Objectives

The project focuses on the following objectives:

- 🎓 Store student information
- ➕ Add new student records
- 📋 Display all student records
- ✏️ Update student age and subjects
- 🗑️ Delete student records
- 📚 Display subjects offered by students
- 🔄 Practise loops and conditional statements
- 🧠 Strengthen Python data-structure concepts

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### ➕ Add Student

Enter student ID, name, age, grade, date of birth, and subjects.

</td>

<td width="50%">

### 📋 Display Students

View the available student records with their stored information.

</td>
</tr>

<tr>
<td width="50%">

### ✏️ Update Student

Search for a student using their ID and update age and subjects.

</td>

<td width="50%">

### 🗑️ Delete Student

Remove a student record using the student's ID.

</td>
</tr>

<tr>
<td width="50%">

### 📚 Display Subjects

Display the subjects stored for the students.

</td>

<td width="50%">

### 🚪 Exit

Exit the Student Data Organizer from the main menu.

</td>
</tr>
</table>

---

# 🧰 Technology Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github" />

</div>

### Core Technologies

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Main programming language |
| 📋 List | Store multiple student records |
| 📖 Dictionary | Store individual student information |
| 🔤 Set | Store subjects without duplicate values |
| 🔄 Loops | Process menu and student records |
| 🔀 Conditional Statements | Handle menu choices and validation |
| ⌨️ Input Handling | Collect student information from the user |

---

# 🏗️ Project Structure

```text
Collection_Manipulation_-Student_Management-_project/
│
├── Collection Manipulation project/
│   └── collection_manipulation_student_managment.py
│
└── readme/
```

> The Python source file is located inside the **Collection Manipulation project** folder.

---

# 🔄 Application Workflow

```text
Start
  │
  ▼
Display Main Menu
  │
  ├── 1. Add Student
  │       │
  │       └── Store Student Details
  │
  ├── 2. Display All Students
  │       │
  │       └── Show Stored Records
  │
  ├── 3. Update Student Information
  │       │
  │       └── Update Age & Subjects
  │
  ├── 4. Delete Student
  │       │
  │       └── Remove Student Record
  │
  ├── 5. Display Subjects Offered
  │       │
  │       └── Show Stored Subjects
  │
  └── 6. Exit
          │
          ▼
         End
```

---

# 📌 Menu Options

| Option | Operation | Description |
|-------:|-----------|-------------|
| 1 | Add Student | Add a new student record |
| 2 | Display all Students | Display stored student information |
| 3 | Update Student Information | Update age and subjects using student ID |
| 4 | Delete Student | Delete a student using student ID |
| 5 | Display Subjects Offered | Display subjects stored in student records |
| 6 | Exit | Close the application |

---

# 🧠 Python Concepts Used

### 📋 Lists

A list is used to store multiple student dictionaries.

```python
student = []
```

### 📖 Dictionaries

Each student record is stored as a dictionary containing:

- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

### 🔤 Sets

Subjects are stored using a set so that repeated subject names are not stored as duplicate values.

```python
sub = {sub.strip() for sub in ssubject.split(",") if sub.strip()}
```

### 🔄 Loops

A `while` loop keeps the main menu running until the user chooses Exit.

A `for` loop is used to search and process student records.

### 🔀 Conditional Statements

`if`, `elif`, and `else` are used to handle different menu choices.

---

# 💻 Example Menu

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display all Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Open the Project Folder

```bash
cd Collection_Manipulation_-Student_Management-_project
```

## 3. Run the Python Program

```bash
python "Collection Manipulation project/collection_manipulation_student_managment.py"
```

---

# 🎥 Project Explanation

Want to understand the project and its working?

▶️ **YouTube Project Explanation:**  
[Watch the Student Management Project Explanation on YouTube](https://youtu.be/KjU1A8uLLY0?si=HqoUWGAiv3Dv2ois)

This video explains the **Collection Manipulation – Student Management** Python project and its working.

---

# 📋 Requirements

This project uses standard Python functionality and does not require external libraries.

### Requirement

- Python 3.x

Check your Python version:

```bash
python --version
```

---

# 📚 What I Learned

Through this project, I practised:

- 🐍 Python fundamentals
- 📋 Lists
- 📖 Dictionaries
- 🔤 Sets
- 🔄 `while` and `for` loops
- 🔀 Conditional statements
- ⌨️ User input handling
- 🔎 Searching records using IDs
- ✏️ Updating stored data
- 🗑️ Deleting list elements
- 🧩 Building a menu-driven CLI application

---

# 🔮 Future Enhancements

Possible improvements for the project:

- 💾 Save student data permanently using file handling
- 🔍 Add student search by name
- 📊 Add marks and percentage management
- 🏆 Add student ranking
- 📑 Export student records to CSV
- 🗄️ Connect the application with a database
- 🖥️ Create a graphical user interface
- 🌐 Convert it into a web-based student management system

---

# 🗺️ Project Roadmap

```text
[████████████████████] 100% Basic Student Management

[████████████████████] 100% Add / Display / Update / Delete

[████████████████████] 100% Subject Management

[██████████░░░░░░░░░░]  50% File Storage

[██████░░░░░░░░░░░░░░]  30% Database Integration

[████░░░░░░░░░░░░░░░░]  20% GUI / Web Application
```

---

# 👨‍💻 About The Developer

<div align="center">

## Parth R. Chauhan

### Computer Engineering Student • Python Learner 

I'm currently learning and building projects in:

```text
Python
   ↓
Data Analysis
 
```

</div>

---

# 🌐 Connect With Me

<div align="center">

### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-Parth--R--Chauhan-181717?style=for-the-badge&logo=github)](https://github.com/Parth-R-Chauhan)

</div>

---

# ⭐ Support The Project

If you found this project useful or interesting:

⭐ **Star** the repository

🍴 **Fork** the repository

💬 **Share** your feedback

🤝 **Connect** with me

---

<div align="center">

## 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=Learn+Python.;Build+Projects.;Solve+Problems.;Keep+Learning+%7C+Keep+Building+%7C+Keep+Growing" alt="Animated Footer"/>

<br><br>

**Made with ❤️ and Python**

</div>
