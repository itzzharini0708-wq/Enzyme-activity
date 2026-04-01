import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.kinetics import michaelis_menten

def enzyme_lab():
    st.header("⚗️ Enzyme Activity Simulator")

    st.markdown("Simulate how enzyme activity changes with substrate concentration.")

    # User Inputs
    Vmax = st.slider("Vmax (maximum rate)", 1.0, 100.0, 50.0)
    Km = st.slider("Km (substrate affinity)", 0.1, 50.0, 10.0)
    substrate = st.slider("Substrate concentration range", 1, 100, 50)

    S = np.linspace(0.1, substrate, 100)
    v = michaelis_menten(S, Vmax, Km)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(S, v)
    ax.set_xlabel("Substrate Concentration [S]")
    ax.set_ylabel("Reaction Rate (v)")
    ax.set_title("Michaelis-Menten Curve")

    st.pyplot(fig)

    # Interpretation
    st.subheader("📊 Interpretation")
    st.write(f"- Higher Vmax → faster maximum reaction rate")
    st.write(f"- Lower Km → higher enzyme affinity for substrate")

    # Quiz / Interaction
    st.subheader("🧠 Quick Check")
    answer = st.radio(
        "What happens when Km is low?",
        ["Low affinity", "High affinity", "No change"]
    )

    if answer == "High affinity":
        st.success("Correct! Lower Km means higher affinity.")
    else:
        st.error("Try again!")