# 🍽️ NutriTrack, an online calorie counter – COSC3506 Final Project

## Team Members
- Cole Della-Savia  
- Godwill Thierry  
- Victor Olojo  
- Gihindu Jeerasinghe  
- Solomon Folowosele  

## 📘 Overview
In today's fast-paced world, many people underestimate their daily calorie intake, often due to overprocessed and calorie-dense foods. This contributes significantly to rising obesity rates, with 1 in 8 individuals living with obesity worldwide.

To tackle this growing concern, our **NutriTrack** project provides a simple and accessible platform for users to:
- Track daily calorie intake  
- Set and monitor personal weight goals  
- Review meal history for better dietary awareness  

This project is a culmination of our work in **COSC3506**, aimed at combining full-stack development practices with practical health applications.

---

## 📌 Scope
The Online Calorie Counter is designed as a full-stack web application, comprising:

### 🔐 User Profiles
Each user has a personalized profile storing:
- Weight goals and target calorie needs
- Logged meals and daily intake history

---

## 🧱 System Architecture

### 🗃️ Database (SQLite)
- Stores user credentials and profile data
  - Unique ID, username, salted & hashed password, optional weight goal
- Stores meal entries
  - Unique meal ID, user ID, required name and calorie count, optional description

### 🔙 Backend (FastAPI – Python)
- **User Authentication**: Secure login and registration
- **Meal Management**: Full CRUD operations for meal data
- **Calorie Tracking**: Retrieve meal history and compute daily calorie totals

### 🎨 Frontend (Vue.js + Vuetify)
- **Login Page**: User sign-in and registration
- **Dashboard**:  
  - Displays goal weight and daily calorie target  
  - Shows total calories consumed today  
  - Lists meals consumed today
- **Meal Entry Screen**:  
  - Add new meals manually  
  - Select from previously logged meals  

---

## ⚙️ Tech Stack

| Layer        | Technology      |
|--------------|-----------------|
| Frontend     | Vue.js, Vuetify |
| Backend      | FastAPI (Python)|
| Database     | SQLite          |
| Version Control | Git + GitHub |

---

## 🔄 Development Methodology
Our team followed the **Agile methodology** to ensure continuous delivery, iterative improvements, and effective collaboration. The project uses a **monolithic architecture** to maintain simplicity and consistency across development.

---

## 🚀 Getting Started

### Clone the Repository, initialise the frontend and backend
```bash
git clone https://github.com/coledella-savia/COSC_Final_Project.git

cd COSC_Final_Project

cd frontend
npm install
npm run dev

cd backend
pip install -r requirements.txt
uvicorn main:app --reload


