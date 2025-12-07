import streamlit as st
import pandas as pd
from database.db import load_opportunities

st.title("📈 Analytics Dashboard")

opps = load_opportunities()

if not opps:
    st.info("No data to analyze yet.")
    st.stop()

df = pd.DataFrame(opps)

st.subheader("Status Distribution")
st.bar_chart(df["status"].value_counts())

st.subheader("Score Distribution")
st.bar_chart(df["score"])
