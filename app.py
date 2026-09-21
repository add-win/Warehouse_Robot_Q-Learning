import streamlit as st
import joblib

model = joblib.load("warehouse_robot_q_table.pkl")

next_states = {
    0: [0, 1, 0, 4],
    1: [0, 2, 1, 5],
    2: [1, 3, 2, 6],
    3: [2, 3, 3, 7],
    4: [4, 5, 0, 8],
    5: [4, 6, 1, 9],
    6: [5, 7, 2, 10],
    7: [6, 7, 3, 11],
    8: [8, 9, 4, 12],
    9: [8, 10, 5, 13],
    10: [9, 11, 6, 14],
    11: [10, 11, 7, 15],
    12: [12, 13, 8, 12],
    13: [12, 14, 9, 13],
    14: [13, 15, 10, 14],
    15: [15, 15, 15, 15]
}

actions = ["LEFT", "RIGHT", "UP", "DOWN"]

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

    best_action_number = q_values.argmax()
    best_action = actions[best_action_number]

    next_state = next_states[state][best_action_number]

    st.subheader("Q-Values")

    st.write("LEFT :", q_values[0])
    st.write("RIGHT :", q_values[1])
    st.write("UP :", q_values[2])
    st.write("DOWN :", q_values[3])

    st.write("Current State:", state)

    st.write("Best Action:", best_action)

    st.write("Next State:", next_state)

    if state == 15:
        st.success("You are currently at the Goal.")

    elif next_state == 15:
        st.success(
            f"The robot should move {best_action} to reach State 15 (GOAL)."
        )
    else:
        st.success(
            f"The robot should move {best_action} to reach State {next_state}."
        )
