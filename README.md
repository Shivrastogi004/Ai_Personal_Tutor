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

## How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/Shivrastogi004/AI_Personal_Tutor.git
cd AI_Personal_Tutor

```
---

Step 2: Install dependencies
Make sure you have Python 3.8+ installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```
---
**Step 4: Run the FastAPI Backend**
To run the FastAPI app (API server):
```bash
python app.py

```
---
uvicorn app:app --reload --host 0.0.0.0 --port 8000
This will start the API at http://0.0.0.0:8000, and you can access the API documentation at http://127.0.0.1:8000/docs.
---
**Step 5: Run the Streamlit App**
To start the Streamlit front-end interface:

```bash
streamlit run streamlit_app.py
```
---
This will open a local Streamlit server at http://localhost:8501 where users can interact with the AI Personal Tutor.
---

**API Endpoints**
1. Predict Knowledge Tracing
POST /predict_knowledge_tracing

Predict whether a student will answer a given problem correctly.

Request Body:
```
json
Copy
{
  "user_id": 1,
  "problem_id": 12,
  "attempt_count": 3,
  "ms_first_response_time": 24000
}
```
Response:
```
json
Copy
{
  "probability_correct": 0.85
}
```
```
2. Recommend Question
POST /recommend_question

Get a recommended question based on the student's previous responses and performance.

Request Body:

json
Copy
{
  "user_id": 1
}
```
```
Response:

json
Copy
{
  "recommended_problem_id": 2
}
```


3. Predict Student Performance
POST /predict_student_performance

Predict a student's performance on a given problem based on various factors like response time, answer choice patterns, and tutor mode used.
```
Request Body:

json
Copy
{
  "attempt_count": 2,
  "ms_first_response_time": 1800,
  "answer_type_choose_1": 1,
  "answer_type_choose_n": 2,
  "answer_type_external": 0,
  "answer_type_fill_in_1": 1,
  "answer_type_open_response": 0,
  "answer_type_rank": 0,
  "tutor_mode_pre": 1,
  "tutor_mode_survey": 0,
  "tutor_mode_test": 1,
  "tutor_mode_tutor": 1
}
```
```
Response:

json
Copy
{
  "predicted_accuracy": 0.72
}

```
---

**Model Overview**
Knowledge Tracing Model: A time-series model built with LSTM (Long Short-Term Memory) to predict if a student will answer a question correctly based on past interactions.

Student Performance Prediction Model: This model uses XGBoost, a decision-tree-based ensemble method, to predict a student's overall performance based on multiple behavioral features.

Question Recommendation Model: The model uses Matrix Factorization (SVD) to recommend questions to the student based on their previous interactions with the system.

Example Use Cases
Predicting Knowledge: When a student enters their performance metrics (e.g., response time, past attempts), the system will predict whether the student is likely to answer a question correctly. This feedback helps the student know if they need further practice in a certain topic.

Personalized Question Recommendations: After a student’s performance is analyzed, the system can recommend personalized questions to help the student improve specific weak areas.

Performance Analysis: The system can predict a student's overall performance based on various metrics, helping tutors or educational institutions understand where a student needs more attention.

Contributing
Feel free to contribute to this project! Whether it's fixing bugs, adding new features, or improving the documentation, your contributions are welcome.

Steps to contribute:
Fork this repository.

Create a new branch for your feature.

Commit your changes.

Push to your fork and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or suggestions, feel free to open an issue or contact the project maintainers directly.

Thank you for using AI Personal Tutor, and we hope it helps you on your educational journey! 🚀

pgsql
Copy

This README is interactive, organized, and provides clear details on how to set up and run the project, along with detailed descriptions of the API endpoints and models used in the project. You can copy and paste this into your `README.md` file.




