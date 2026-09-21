import streamlit as st
import joblib
import pandas as pd

model = joblib.load("warehouse_robot_q_table.pkl")

st.title("Warehouse Robot Q-Learning")

state = st.number_input(
    "Enter the Robot State",
    min_value=0,
    max_value=15,
    value=0,
    step=1
)

if st.button("Find Best Action"):

    q_values = model[state]

    q_table = pd.DataFrame({
        "Action": ["LEFT", "RIGHT", "UP", "DOWN"],
        "Q-value": q_values
    })

    st.subheader("Q-Values")
    st.dataframe(q_table)

    best_action = ["LEFT", "RIGHT", "UP", "DOWN"][q_values.argmax()]

    st.subheader("Best Action")

    st.success(f"The robot should move {best_action}.")
