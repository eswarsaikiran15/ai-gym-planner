import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 🔥 Enhance Accuracy: Larger Fitness Dataset
data = {
    "Weight": [50, 60, 70, 80, 90, 100, 110, 75, 85, 95, 105, 115, 55, 65, 77],
    "Exercise_Duration": [20, 30, 45, 60, 40, 25, 35, 50, 60, 70, 45, 30, 50, 55, 65],
    "Exercise_Type": [1, 2, 1, 3, 2, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1],  # 1: Cardio, 2: Strength, 3: Mixed
    "Calories_Burned": [120, 220, 300, 450, 380, 200, 310, 420, 500, 600, 460, 280, 470, 390, 360]
}

df = pd.DataFrame(data)

# 🔥 Train ML Model
X = df.drop(columns=["Calories_Burned"])
y = df["Calories_Burned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🎨 Streamlit UI
st.set_page_config(page_title="AI Gym Planner", page_icon="💪", layout="centered")



st.title("🏋️ AI Gym Planner - Calorie Burn Prediction")
st.write("🔹 Get **calories burned** estimate & personalized **workout plan**!")

# 🎯 User Inputs
weight = st.slider("Select your weight (kg)", min_value=40, max_value=150, value=70)
duration = st.slider("Select exercise duration (minutes)", min_value=10, max_value=120, value=30)
exercise_type = st.selectbox("Choose Exercise Type", ["Cardio", "Strength", "Mixed"])

# Convert Exercise Type to Number
exercise_mapping = {"Cardio": 1, "Strength": 2, "Mixed": 3}
exercise_type_num = exercise_mapping[exercise_type]

# 🚀 Prediction Function
def predict_calories(weight, duration, exercise_type):
    return model.predict([[weight, duration, exercise_type]])[0]

# 🔥 Predict Calories Burned
if st.button("🔍 Predict Calories Burned"):
    calories = predict_calories(weight, duration, exercise_type_num)
    st.success(f"🔥 Estimated Calories Burned: **{calories:.2f} kcal**")

    # 🎯 Recommended Workout Plan
    st.subheader("🏋️‍♂️ Personalized Workout Plan")
    if exercise_type == "Cardio":
        st.write("- 🏃 **Treadmill**: 20-30 mins")
        st.write("- 🚴 **Cycling**: 30 mins")
        st.write("- 🦵 **Jump Rope**: 10 mins")
    elif exercise_type == "Strength":
        st.write("- 🏋️ **Deadlifts**: 3 sets of 10 reps")
        st.write("- 🏋️ **Bench Press**: 3 sets of 8 reps")
        st.write("- 🏋️ **Squats**: 3 sets of 12 reps")
    else:
        st.write("- ⚡ **HIIT (High-Intensity Interval Training)**: 30 mins")
        st.write("- 💪 **Burpees, Push-ups, Planks**: 3 rounds")

    # 🎨 Show Progress Graph
    st.subheader("📊 Calories Burned Over Time")
    progress_df = pd.DataFrame({"Day": range(1, 11), "Calories": np.random.randint(200, 600, 10)})
    fig, ax = plt.subplots()
    sns.lineplot(data=progress_df, x="Day", y="Calories", marker="o", linewidth=2, ax=ax)
    st.pyplot(fig)

