# SnapClass – AI-Powered Attendance Management System

An intelligent attendance management platform that simplifies classroom attendance using face recognition and voice processing.

SnapClass helps teachers manage subjects, enroll students and record attendance through an integrated web application, while giving students a convenient way to access their enrolled subjects and attendance information.

## 🚀 Key Features

### 👨‍🏫 Teacher Dashboard
- Teacher authentication.
- Create and manage subjects.
- Manage enrolled students.
- Take attendance using AI-powered face and voice processing.
- View attendance records.

### 👨‍🎓 Student Dashboard
- Student access and authentication.
- View enrolled subjects.
- Join subjects using a unique join code.
- Track attendance information.

### 🤖 AI-Powered Attendance

- Face embedding extraction and recognition.
- Machine-learning-based face classification.
- Voice embedding extraction and processing.
- Automated attendance workflow.

### 🔗 Quick Enrollment
- Generate subject-specific join links.
- Share QR codes with students.
- Allow students to enroll in subjects using a join code.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| Database | Supabase |
| Machine Learning | Scikit-learn |
| Face Processing | face_recognition, dlib |
| Voice Processing | Resemblyzer, librosa |
| Data Processing | NumPy, Pandas |
| Authentication | bcrypt |
| QR Code Generation | segno |
| Version Control | Git, GitHub |

## 🏗️ Project Architecture

The application follows a modular structure separating the user interface, processing pipelines and database operations.

```text
SnapClass/
│
├── app.py
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   └── ui/
│
├── requirements.txt
├── .gitignore
└── README.md
```

- **UI Layer:** Streamlit screens and reusable interface components.
- **Processing Layer:** Face and voice processing pipelines.
- **Database Layer:** Supabase database operations and data management.
- **Application Layer:** Authentication, navigation and attendance workflows.

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User] --> B[Streamlit Application]
    B --> C[Teacher Dashboard]
    B --> D[Student Dashboard]

    C --> E[Face Attendance Pipeline]
    C --> F[Voice Attendance Pipeline]

    E --> G[Face Embeddings and ML Model]
    F --> H[Voice Embeddings]

    D --> I[Student Enrollment]
    I --> J[Supabase Database]

    G --> J
    H --> J
    J --> K[Attendance Records]

## ⚙️ Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/ShubhamMishra-TechBuildS/MDU-Attendance-Portal-main.git

cd MDU-Attendance-Portal-main
```

### 2. Create a virtual environment

```
python -m venv venv
```

Activate it on Windows:

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure Supabase

Create a Supabase project and configure the required database connection credentials.

Keep credentials in environment variables or Streamlit secrets. Never commit private keys or passwords to GitHub.

Use the configuration variable names expected by the application's database module.

### 5. Run the application

```
streamlit run app.py
```

## 🧠 How It Works

1. Teachers and students access the application through their respective interfaces.
2. Teachers create subjects and share enrollment links or QR codes.
3. Students join subjects using the provided enrollment code.
4. The application processes face and voice inputs through its respective pipelines.
5. Attendance information is stored and made available through the application.

## 🎯 Project Objective

The objective of SnapClass is to make classroom attendance more efficient by integrating machine-learning-based face recognition and voice processing into a centralized attendance management platform.

## 👨‍💻 Developer

**Shubham Kumar Mishra**

B.Tech Computer Science and Engineering Student

GitHub: [ShubhamMishra-TechBuildS](https://github.com/ShubhamMishra-TechBuildS)

LinkedIn: [Connect with me](https://www.linkedin.com/in/shubhamkmishra-cs)

---

*Built with Python, Machine Learning and Streamlit.*
