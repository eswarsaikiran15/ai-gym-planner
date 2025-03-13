
view live demo: https://ai-gym-planner-1506.streamlit.app/


#  AI Gym Planner - Calorie Burn Prediction

##  Overview

The **AI Gym Planner** is a Streamlit-based machine learning web application that predicts **calories burned** based on weight, exercise duration, and exercise type. It also provides personalized **workout recommendations** and visualizes calorie-burning progress over time.

##  Features

- **Calorie Burn Prediction**: Uses a trained Random Forest Regressor model.
    
- **Personalized Workout Plan**: Recommends exercises based on user input.
    
- **Interactive UI**: Built with Streamlit for an intuitive experience.
    
- **Progress Graph**: Displays calories burned over time using Matplotlib & Seaborn.
    

##  Technologies Used

- **Python**
    
- **Streamlit**
    
- **Pandas**
    
- **NumPy**
    
- **Matplotlib**
    
- **Seaborn**
    
- **Scikit-Learn**
    

##  Project Structure

```
📁 AI-Gym-Planner
│── app.py               # Main Streamlit application
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

##  Installation & Setup

1. **Clone the repository**:
    
    ```
    git clone https://github.com/eswarsaikiran15/AI-Gym-Planner.git
    cd AI-Gym-Planner
    ```
    
2. **Create a virtual environment** (optional but recommended):
    
    ```
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```
    
3. **Install dependencies**:
    
    ```
    pip install -r requirements.txt
    ```
    
4. **Run the app**:
    
    ```
    streamlit run app.py
    ```
    

##  Usage

1. **Adjust sliders** to set your weight and exercise duration.
    
2. **Select the exercise type** (Cardio, Strength, or Mixed).
    
3. Click on **"Predict Calories Burned"** to get an estimate.
    
4. View your **personalized workout plan** and **progress graph**.
    

##  Sample Data

|Weight (kg)|Exercise Duration (mins)|Exercise Type|Calories Burned|
|---|---|---|---|
|70|45|Cardio|300|
|80|60|Mixed|450|
|90|40|Strength|380|

## **Summary of Steps**

1. **Import Libraries**
2. **Create Dataset**
3. **Train Machine Learning Model**
    - Split data into `X` and `y`
    - Use `train_test_split()`
    - Train `RandomForestRegressor`
4. **Build Streamlit UI**
    - Title & description
    - Collect user input via sliders & dropdown
    - Convert exercise type to numbers
5. **Make Predictions**
    - Use trained model to predict `Calories_Burned`
6. **Provide Personalized Workout Plan**
7. **Display Progress Chart (Calories Burned Over Time)**

##  Machine Learning Model

- Uses **RandomForestRegressor** for calorie burn prediction.
    
- Trained on sample fitness data with features:
    
    - **Weight** (kg)
        
    - **Exercise Duration** (minutes)
        
    - **Exercise Type** (Cardio, Strength, Mixed)
        

##  Future Enhancements

- Expand the dataset for better model accuracy.
    
- Implement real-time tracking of workout data.
    
- Add AI-powered personalized fitness plans.
