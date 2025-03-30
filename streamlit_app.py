import streamlit as st
import numpy as np
import time
import tensorflow as tf
import xgboost as xgb
import pickle
import openai
import os

# Load the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load the models directly into Streamlit
@st.cache_resource
def load_lstm_model():
    lstm_model = tf.keras.models.load_model("knowledge_tracing_lstm.h5")
    return lstm_model

@st.cache_resource
def load_xgb_model():
    xgb_model = xgb.XGBRegressor()
    xgb_model.load_model("student_performance_prediction_xgb.json")
    return xgb_model

@st.cache_resource
def load_question_recommendation_model():
    with open("adaptive_question_recommendation_svd.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Load models into Streamlit
lstm_model = load_lstm_model()
xgb_model = load_xgb_model()
question_recommendation_model = load_question_recommendation_model()

# Streamlit UI Setup
st.title("AI Personal Tutor")

# 1. Predict Knowledge Tracing (Will the student answer correctly?)
st.header("Predict Knowledge Tracing")

# User Inputs
user_id = st.number_input("User ID", min_value=1, step=1)
problem_id = st.number_input("Problem ID", min_value=1, step=1)
attempt_count = st.number_input("Attempt Count", min_value=1, step=1)
ms_first_response_time = st.number_input("Response Time (ms)", min_value=0.0)

# Button to trigger prediction for Knowledge Tracing
if st.button("Predict if Answer is Correct"):
    with st.spinner("Predicting..."):
        # Prepare the data to be sent as input
        input_data = np.array([[user_id, problem_id, attempt_count, ms_first_response_time]])
        input_data = np.expand_dims(input_data, axis=-1)  # Reshape for LSTM
        
        # Make prediction using the LSTM model
        probability = lstm_model.predict(input_data)[0][0]
        
        # Display Prediction Result
        st.write(f"Prediction Result: Probability of Correct Answer = {probability:.2f}")
        
        # Provide feedback based on prediction probability
        if probability > 0.8:
            st.markdown("### 🔥 Strong Knowledge!")
            st.write("You have a high probability of answering correctly. Keep up the great work!")
        elif 0.5 <= probability <= 0.8:
            st.markdown("### ⚠️ Needs Refinement!")
            st.write("Your knowledge is good, but some areas need refining. Keep practicing!")
        else:
            st.markdown("### ❗ Refine Knowledge")
            st.write("It seems you need to improve in this area. Please review the material again.")

    # Add a bit of delay before showing the next recommendation (simulating an interactive animation)
    time.sleep(1)

# 2. Recommend Question (Personalized Recommendations)
st.header("Recommend a Question")

# Button to fetch recommended question after knowledge prediction
if st.button("Get Recommended Question"):
    with st.spinner("Fetching recommendation..."):
        # Simulate the recommendation process (replace with actual logic from your model)
        predictions = np.random.rand(10)  # Replace with actual model predictions
        recommended_question = int(np.argmax(predictions))  # Get question with highest prediction
        
        # Display the recommended question ID
        st.write(f"Recommended Question ID: {recommended_question}")
        st.markdown("### ✨ Here's a question to help refine your knowledge!")
        
        # Show a sample question (can replace this with your actual question data)
        st.write(f"**Sample Question {recommended_question}:** What is the derivative of sin(x)?")

        # Feedback for the recommended topic
        st.markdown("### Study Topic Feedback:")

        if recommended_question % 2 == 0:
            st.write("This topic involves **calculus**. You might want to review **derivatives and their properties**. Here's a helpful resource: [Khan Academy - Derivatives](https://www.khanacademy.org/math/calculus-1)")
        else:
            st.write("This topic involves **trigonometry**. You might want to review **trigonometric identities and their applications**. Here's a helpful resource: [Khan Academy - Trigonometry](https://www.khanacademy.org/math/trigonometry)")

        st.write("You can review this topic to improve your knowledge and refine your skills.")

# 3. Predict Student Performance (Accuracy Prediction)
st.header("Predict Student Performance")

# Performance-related inputs
attempt_count_perf = st.number_input(
    "How many times have you attempted this type of question?", 
    min_value=1, step=1, 
    help="Enter how many attempts you've made for this type of question."
)

ms_first_response_time_perf = st.number_input(
    "How long did it take you to respond (in milliseconds)?", 
    min_value=0.0, 
    help="Enter the time it took for you to answer the question (in milliseconds)."
)

answer_type_choose_1 = st.number_input(
    "How often do you choose the first answer option?", 
    min_value=0, step=1, 
    help="How frequently do you select the first answer choice?"
)

answer_type_choose_n = st.number_input(
    "How often do you choose the last answer option?", 
    min_value=0, step=1, 
    help="How frequently do you select the last answer choice?"
)

answer_type_external = st.number_input(
    "How often do you answer using external resources?", 
    min_value=0, step=1, 
    help="How frequently do you refer to external resources like textbooks or internet?"
)

answer_type_fill_in_1 = st.number_input(
    "How often do you fill in the first blank in fill-in-the-blank questions?", 
    min_value=0, step=1, 
    help="How often do you attempt to answer fill-in-the-blank questions?"
)

answer_type_open_response = st.number_input(
    "How often do you answer open-ended questions?", 
    min_value=0, step=1, 
    help="How frequently do you attempt open-ended or essay-based questions?"
)

answer_type_rank = st.number_input(
    "How often do you rank answers in multiple-choice questions?", 
    min_value=0, step=1, 
    help="How often do you rank answers from best to worst in multiple-choice?"
)

tutor_mode_pre = st.number_input(
    "How often do you use pre-assessment tools?", 
    min_value=0, step=1, 
    help="How often do you use pre-assessments or quizzes before the lesson?"
)

tutor_mode_survey = st.number_input(
    "How often do you use survey-based learning?", 
    min_value=0, step=1, 
    help="How often do you answer surveys to reflect on your learning?"
)

tutor_mode_test = st.number_input(
    "How often do you participate in tests?", 
    min_value=0, step=1, 
    help="How often do you take tests or mock exams?"
)

tutor_mode_tutor = st.number_input(
    "How often do you have a tutor or instructor review your work?", 
    min_value=0, step=1, 
    help="How often do you seek help from a tutor or instructor?"
)

# Button to trigger performance prediction
if st.button("Predict Student Performance"):
    with st.spinner("Predicting Performance..."):
        # Construct the input array for performance prediction
        input_data = np.array([[
            attempt_count_perf, ms_first_response_time_perf,
            answer_type_choose_1, answer_type_choose_n, answer_type_external,
            answer_type_fill_in_1, answer_type_open_response, answer_type_rank,
            tutor_mode_pre, tutor_mode_survey, tutor_mode_test, tutor_mode_tutor
        ]])

        # Make prediction using the XGBoost model for student performance
        predicted_performance = xgb_model.predict(input_data)
        
        # Display predicted accuracy
        st.write(f"Predicted Performance Accuracy: {predicted_performance[0]:.2f}")

        # Provide feedback based on performance prediction
        accuracy = predicted_performance[0]
        if accuracy > 0.8:
            st.markdown("### 🔥 Strong Performance!")
            st.write("You are performing very well. Keep up the excellent work!")
        elif 0.5 <= accuracy <= 0.8:
            st.markdown("### ⚠️ Needs Improvement!")
            st.write("You are performing decently, but there's room for improvement. Review your weak areas.")
        else:
            st.markdown("### ❗ Performance Needs Attention")
            st.write("Your performance needs attention. Consider focusing on the topics where you are struggling.")
