import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("data/country_scores.csv")

# App title
st.title("Country Economic Score Viewer")

# Slider for score filtering
threshold = st.slider("Highlight countries with score above:", 0, 100, 70)

# Show full data
st.subheader("All Country Scores")
st.dataframe(df)

# Show filtered data
st.subheader(f"Countries with Score > {threshold}")
st.dataframe(df[df["Score"] > threshold])
