# AI Personal Tutor

Welcome to the **AI Personal Tutor** repository! This project aims to build an interactive and intelligent tutoring system powered by AI, leveraging various machine learning models to predict student performance, recommend personalized questions, and track their learning progress. The AI tutor is designed to help students improve their understanding and performance in various academic subjects by offering adaptive learning experiences.

## Features

1. **Knowledge Tracing**
   - Predicts whether a student will answer a question correctly based on their past performance, behavior, and time spent on the question.
   - Uses a Long Short-Term Memory (LSTM) model for time-series predictions.
   
2. **Personalized Question Recommendations**
   - Recommends personalized questions based on the student's previous answers and engagement.
   - Uses a **Matrix Factorization** model (SVD) to generate question recommendations.

3. **Student Performance Prediction**
   - Predicts the student's performance based on multiple features like response time, answer choice patterns, and interaction with various tutor modes.
   - Uses **XGBoost** for performance prediction.

## Technologies Used

- **Backend**: 
   - **FastAPI** for API development.
   - **TensorFlow (LSTM)** for knowledge tracing.
   - **XGBoost** for student performance prediction.
   - **Pickle** for question recommendation model.
   - **OpenAI API** for text processing and interactive feedback.

- **Frontend**:
   - **Streamlit** for building the user interface of the AI-powered tutor.

---

## Step 1: Clone the Repository

To begin setting up the **AI Personal Tutor**, first, clone the repository using the following command:

```bash
git clone https://github.com/Shivrastogi004/AI_Personal_Tutor.git
cd AI_Personal_Tutor
```
---
## Step 2: Install Dependencies

Make sure you have **Python 3.8+** installed. Then, install the required libraries by running the following command in your project directory:

```bash
pip install -r requirements.txt
```
---
## Step 3: Run the FastAPI Backend

To start the FastAPI app (API server), use the following command:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
---
### Screenshot of FastAPI Documentation:
![FastAPI Documentation](Screenshot/Screenshot_2025-03-31_143017.png)

### Screenshot of FastAPI Response:
![FastAPI Response](Screenshot/Screenshot_2025-03-31_143030.png)

### Screenshot of FastAPI Parameters:
![FastAPI Parameters](Screenshot/Screenshot_2025-03-31_143037.png)

### Screenshot of FastAPI Request Body:
![FastAPI Request Body](Screenshot/Screenshot_2025-03-31_143100.png)

### Screenshot of FastAPI Error Response:
![FastAPI Error Response](Screenshot/Screenshot_2025-03-31_143105.png)


