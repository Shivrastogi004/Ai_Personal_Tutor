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
![FastAPI Documentation](Screenshot/Screenshot%202025-03-31%20143017.png)
---
### Screenshot of FastAPI Response:
![FastAPI Response](Screenshot/Screenshot%202025-03-31%20143030.png)
---
### Screenshot of FastAPI Parameters:
![FastAPI Parameters](Screenshot/Screenshot%202025-03-31%20143037.png)
---
### Screenshot of FastAPI Request Body:
![FastAPI Request Body](Screenshot/Screenshot%202025-03-31%20143100.png)
---
### Screenshot of FastAPI Error Response:
![FastAPI Error Response](Screenshot/Screenshot%202025-03-31%20143105.png)

---
## Step 4: Run the Streamlit Frontend

Once the FastAPI backend is up and running, you can start the Streamlit frontend by executing the following command:

```bash
streamlit run streamlit_app.py
```
---
### Screenshot of Streamlit Interface:
![Streamlit Interface 1](Screenshot/Screenshot%202025-03-31%20142736.png)
---
### Screenshot of Streamlit Interface 2:
![Streamlit Interface 2](Screenshot/Screenshot%202025-03-31%20142756.png)
---
### Screenshot of Streamlit Interface 3:
![Streamlit Interface 3](Screenshot/Screenshot%202025-03-31%20142808.png)
---
### Screenshot of Streamlit Interface 4:
![Streamlit Interface 4](Screenshot/Screenshot%202025-03-31%20142824.png)
---
### Screenshot of Streamlit Interface 5:
![Streamlit Interface 5](Screenshot/Screenshot%202025-03-31%20142833.png)
---
### Screenshot of Streamlit Interface 6:
![Streamlit Interface 6](Screenshot/Screenshot%202025-03-31%20142843.png)

---
## Step 5: Test the AI Personal Tutor

Once everything is set up, you can test the **AI Personal Tutor** by interacting with the frontend. The application will allow you to:

- Predict a student's performance based on various input parameters such as response time, answer choice patterns, and more.
- Receive personalized question recommendations to improve knowledge retention.
- Track the learning progress of the student over time.

Test various parameters and see how the AI adapts to the user inputs.

### Example Inputs:
- **User ID**
- **Problem ID**
- **Attempt Count**
- **Response Time (ms)**

These inputs are processed by the backend to predict the performance and offer recommendations.

---

## Conclusion

The **AI Personal Tutor** is an advanced, AI-driven platform that leverages machine learning models to personalize learning and predict student performance. By integrating models like **LSTM** for knowledge tracing, **XGBoost** for performance prediction, and **Matrix Factorization** for personalized question recommendations, this project enhances the student learning experience.

With the setup complete and the system running, students and educators can use the AI tutor for real-time analysis, performance tracking, and content personalization.

We hope this platform helps improve student engagement and learning outcomes, making it easier for educators to provide tailored learning experiences.

---

## Summary Table

Here is a quick summary of the steps involved in setting up and running the **AI Personal Tutor**:

| **Step** | **Description**                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------|
| **Step 1**   | **Clone the Repository**: Download the project files to your local machine.                           |
| **Step 2**   | **Install Dependencies**: Install all required Python libraries using the `requirements.txt` file.     |
| **Step 3**   | **Run the FastAPI Backend**: Start the FastAPI server to handle API requests for performance prediction.|
| **Step 4**   | **Run the Streamlit Frontend**: Launch the Streamlit app for user interaction and input processing.     |
| **Step 5**   | **Test the AI Personal Tutor**: Interact with the tutor, input various parameters, and test the system. |

Refer RELEASES for EDnet 4 compatible files and information 

---

Dataset avaialable for download as a zip file directly.

---








