import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.cooling_curve import generate_cooling_curve
from src.analysis import load_cct_data, basic_summary

st.set_page_config(page_title="TTT/CCT Diagram Analyzer", layout="wide")

st.title("TTT/CCT Diagram Analyzer")
st.write("Educational tool for visualizing a simplified CCT transformation diagram and cooling curve.")

steel_grade = st.selectbox("Steel Grade", ["AISI 4140", "AISI 1045", "AISI 4340"])
initial_temperature = st.number_input(
    "Initial Austenitizing Temperature (°C)", min_value=700, max_value=1200, value=850
)
cooling_rate = st.number_input(
    "Cooling Rate (°C/s)", min_value=0.1, max_value=100.0, value=10.0
)
duration = st.number_input(
    "Cooling Duration (s)", min_value=10, max_value=1000, value=100
)

data = load_cct_data("data/cct_data.csv")
summary = basic_summary(data)

st.subheader("CCT Diagram")

fig, ax = plt.subplots(figsize=(9, 5))

for transformation in data["transformation"].unique():
    subset = data[data["transformation"] == transformation]
    ax.scatter(subset["time"], subset["temperature"], label=transformation, s=60)

time, temperature = generate_cooling_curve(
    initial_temperature, cooling_rate, duration
)
ax.plot(time, temperature, label="Cooling Curve")

ax.set_xscale("log")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (°C)")
ax.set_title(f"Simplified CCT Visualization — {steel_grade}")
ax.grid(True, which="both")
ax.legend()

st.pyplot(fig)

st.subheader("Summary")
col1, col2 = st.columns(2)
col1.metric("Number of data points", summary["points"])
col2.metric("Minimum temperature", f'{summary["min_temperature"]:.0f} °C')

st.subheader("CCT Data")
st.dataframe(data, use_container_width=True)


