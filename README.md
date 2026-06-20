Vikshit Bihar AI Chatbot

🚀 Live Demo: https://vikshit-bihar-chatbot-1.onrender.com

Overview

Vikshit Bihar AI Chatbot is an AI-powered educational analytics platform developed using FastAPI, MySQL, Google Gemini, and a custom frontend interface. The chatbot enables users to ask questions in natural language and receive accurate, database-driven answers from educational datasets.

The system automatically converts user questions into SQL queries, retrieves relevant information from the database, and generates human-readable responses using Google Gemini.

---

Features

- Natural Language Question Answering
- AI-Powered SQL Query Generation
- Google Gemini Integration
- Lightweight RAG Architecture
- FastAPI REST API Backend
- MySQL Database Integration
- Student Admission Analytics
- Placement Statistics
- Branch-wise Registration Reports
- Professor Statistics
- Hostel and Bed Availability Analysis
- Responsive Frontend Interface
- Dynamic Database Schema Retrieval

---

Live Demo

https://vikshit-bihar-chatbot-1.onrender.com

---

Technology Stack

Frontend

- HTML
- CSS
- JavaScript

Backend

- FastAPI
- Python

Database

- MySQL

Artificial Intelligence

- Google Gemini 2.5 Flash

Tools & Platforms

- VS Code
- DBeaver
- Git
- GitHub
- Render

---

LLM and RAG Implementation

Large Language Model (LLM)

This project uses Google Gemini 2.5 Flash as the Large Language Model (LLM).

The LLM is responsible for:

- Understanding user questions
- Analyzing database schema
- Generating SQL queries
- Producing human-readable responses

Retrieval-Augmented Generation (RAG)

The chatbot follows a lightweight RAG approach.

Before generating SQL queries, the system retrieves database metadata including:

- Table names
- Column names
- Database schema information

The retrieved schema is then passed to Gemini as context.

RAG Workflow

User Question
      │
      ▼
Schema Retrieval
(SHOW TABLES + DESCRIBE)
      │
      ▼
Retrieved Context
      │
      ▼
Gemini LLM
      │
      ▼
SQL Query Generation
      │
      ▼
MySQL Database
      │
      ▼
Query Result
      │
      ▼
Gemini LLM
      │
      ▼
Natural Language Response

Benefits

- Improved SQL Accuracy
- Reduced Hallucinations
- Database-Aware Responses
- Dynamic Query Generation
- Reliable Data-Driven Answers

---

System Architecture

User
 │
 ▼
Frontend (HTML/CSS/JavaScript)
 │
 ▼
FastAPI Backend
 │
 ▼
Gemini AI
 │
 ▼
SQL Query Generation
 │
 ▼
MySQL Database
 │
 ▼
Query Result
 │
 ▼
Gemini AI
 │
 ▼
Response Generation
 │
 ▼
Frontend Display

---

Project Structure

Vikshit_bihar_chatbot/
│
├── main.py
├── database.py
├── gemini_service.py
├── check.py
├── requirements.txt
├── .env
├── .gitignore
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   ├── student_admission_report_year_wise_district_wise.csv
│   ├── student_placement_report_year_wise.csv
│   ├── number_of_registered_students_branch_wise_year_wise.csv
│   ├── professor_statistics_college_wise_branch_wise_district_wise.csv
│   └── number_of_available_hostel_and_beds_district_wise.csv
│
└── README.md

File Description

File / Folder| Description
"main.py"| Main FastAPI application containing API routes and chatbot logic.
"database.py"| Handles MySQL database connection and query execution.
"gemini_service.py"| Integrates Google Gemini for SQL generation and response generation.
"check.py"| Used for testing Gemini API connectivity.
"requirements.txt"| Contains required Python dependencies.
".env"| Stores API keys and database credentials.
".gitignore"| Prevents sensitive files from being pushed to GitHub.
"frontend/index.html"| Main chatbot interface.
"frontend/style.css"| User interface styling and responsiveness.
"frontend/script.js"| Handles API requests and UI updates.
"student_admission_report_year_wise_district_wise.csv"| Admission statistics dataset.
"student_placement_report_year_wise.csv"| Placement statistics dataset.
"number_of_registered_students_branch_wise_year_wise.csv"| Registration statistics dataset.
"professor_statistics_college_wise_branch_wise_district_wise.csv"| Professor statistics dataset.
"number_of_available_hostel_and_beds_district_wise.csv"| Hostel and bed availability dataset.
"README.md"| Project documentation.

---

Installation

Clone Repository

git clone https://github.com/divyanshikumari/Vikshit_bihar_chatbot.git
cd Vikshit_bihar_chatbot

Create Virtual Environment

python -m venv venv

Activate Environment

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Create a ".env" file:

GEMINI_API_KEY=your_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=bihar_chatbot

Run FastAPI Server

uvicorn main:app --reload

---

API Endpoints

Home

GET /

Database Tables

GET /tables

Chatbot Endpoint

POST /chat

Example Request:

{
  "question": "How many students are registered in Computer Science And Engineering?"
}

Example Response:

{
  "answer": "The total number of registered students in Computer Science And Engineering is 6825."
}

---

API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

---

Future Enhancements

- Voice Assistant Integration
- Multilingual Support
- Dashboard Analytics
- Interactive Data Visualization
- Authentication & Authorization
- Real-Time Reporting
- Mobile Application Support

---

Author

Developed by Divyanshi Kumari
