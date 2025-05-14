import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import os

# Use absolute paths
base_path = os.path.dirname(__file__)
state_df = pd.read_csv(os.path.join(base_path, "state_risk_scores.csv"))
client_df = pd.read_csv(os.path.join(base_path, "client_location_risks.csv"))

# Title
st.title("Earthquake Risk Assessment Dashboard")

# Section 1: State Risk Table
st.header("State-Level Earthquake Risk")
st.dataframe(state_df)

# Section 2: Bar Chart
st.header("Risk Score by State")
fig, ax = plt.subplots()
ax.bar(state_df["state"], state_df["risk_score"], color='skyblue')
ax.set_xlabel("State")
ax.set_ylabel("Risk Score")
ax.set_title("Earthquake Risk Score by State")
st.pyplot(fig)

# Section 3: Client Locations Map
st.header("Client Locations on Map")
m = folium.Map(location=[40, -115], zoom_start=4)
for _, row in client_df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=f"Challis High School\nIdaho\nRisk Score: 4.2"
    ).add_to(m)
folium_static(m)

# Section 4: Client Table
st.header("Client Location Risk Table")
st.dataframe(client_df)
