# Warehouse Robot Q-Learning

A simple interactive web app that demonstrates a warehouse robot learning the best movement policy using a Q-learning table. The app loads a trained Q-table, lets the user choose a robot state, and shows the best action to take next.

## Project Overview

This project models a warehouse grid where a robot moves between states and learns which action leads to the best outcome. The trained model uses a Q-table to predict the most valuable action for a given state.

The app is built with Streamlit and shows:

- the Q-values for each action
- the best action for the selected state
- the next state reached by that action
- a goal check when the robot is already at the target state

## Features

- Interactive robot state input
- Q-value table display
- Best action recommendation
- Goal-state detection
- Lightweight dashboard UI powered by Streamlit

## Tech Stack

- Python
- Streamlit
- pandas
- joblib
- scikit-learn
- numpy

## Project Structure

- `app.py` — Streamlit app for interacting with the trained Q-table
- `requirements.txt` — project dependencies
- `warehouse_robot_q_table.pkl` — pre-trained Q-table model

## Setup

1. Clone the repository.
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal in your browser.

## How It Works

1. The app loads a saved Q-table from `warehouse_robot_q_table.pkl`.
2. The user enters a robot state between 0 and 15.
3. The app reads the Q-values for each possible action.
4. The action with the highest Q-value is selected as the best move.
5. The app displays the recommended move and the resulting target state.

## Example Use

If the robot is in a state near the goal, the app will recommend the action that leads toward the target state and show a success message when the goal is reached.

## Suggested Project Names

Here are some strong names for the project:

- WarehouseBot Q-Learning
- Smart Warehouse Navigator
- QGrid Warehouse Robot
- Warehouse Robot Planner
- RobotPath Optimizer
- WarehouseIQ Navigator

### Best fit

**WarehouseBot Q-Learning** is the most clear and professional name for this project.

## License

This project is for educational and demonstration purposes.
