from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf

# Initialize FastAPI app
app = FastAPI()

# Load trained models
knowledge_tracing_model = tf.keras.models.load_model("knowledge_tracing_lstm.h5")

# Pydantic model for request body validation
class KnowledgeTracingRequest(BaseModel):
    user_id: int
    problem_id: int
    attempt_count: int
    ms_first_response_time: float

# Root route to handle 404 errors
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Tutor API! Access the documentation at /docs"}

# API Endpoint 1: Predict if a student will answer correctly
@app.post("/predict_knowledge_tracing")
def predict_knowledge_tracing(request: KnowledgeTracingRequest):
    # Extract the data from the request
    user_id = request.user_id
    problem_id = request.problem_id
    attempt_count = request.attempt_count
    ms_first_response_time = request.ms_first_response_time
    
    # Prepare input data for the LSTM model
    input_data = np.array([[user_id, problem_id, attempt_count, ms_first_response_time]])
    input_data = np.expand_dims(input_data, axis=-1)  # Reshape for LSTM
    
    # Make prediction using the LSTM model
    prediction = knowledge_tracing_model.predict(input_data)
    
    # Return the result as a JSON response
    return {"probability_correct": float(prediction[0][0])}

@app.post("/recommend_question")
def recommend_question(user_id: int):
    try:
        # Ensure user_id exists in Q_table
        if user_id not in range(Q_table.shape[0]):
            return {"error": "User ID not found in Q_table"}
        
        # Generate predictions for all questions for the given user
        predictions = [
            question_recommendation_model.predict(user_id, problem).est
            for problem in range(Q_table.shape[1])
        ]

        # Find the best recommended problem
        recommended_question = int(np.argmax(predictions))

        return {"recommended_problem_id": recommended_question}

    except Exception as e:
        return {"error": str(e)}

@app.post("/predict_student_performance")
def predict_student_performance(
    attempt_count: int, ms_first_response_time: float,
    answer_type_choose_1: int, answer_type_choose_n: int, answer_type_external: int,
    answer_type_fill_in_1: int, answer_type_open_response: int, answer_type_rank: int,
    tutor_mode_pre: int, tutor_mode_survey: int, tutor_mode_test: int, tutor_mode_tutor: int
):
    try:
        # Log received values
        print(f"🔹 Received Input: {locals()}")

        # Construct the input array
        input_data = np.array([[
            attempt_count, ms_first_response_time,
            answer_type_choose_1, answer_type_choose_n, answer_type_external,
            answer_type_fill_in_1, answer_type_open_response, answer_type_rank,
            tutor_mode_pre, tutor_mode_survey, tutor_mode_test, tutor_mode_tutor
        ]])

        print(f"✅ Input Data Shape: {input_data.shape}, Expected: (1, 12)")

        # Ensure shape matches model expectation
        if input_data.shape[1] != 12:
            return {"error": "Feature shape mismatch. Expected 12 features, got {input_data.shape[1]}"}

        # Make prediction
        predicted_performance = student_performance_model.predict(input_data)
        return {"predicted_accuracy": float(predicted_performance[0])}

    except Exception as e:
        print(f"❌ Error: {e}")
        return {"error": str(e)}

# Run FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
