
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Indian EV Market Dashboard", layout="wide")

st.title("🔋 Indian EV Market Dashboard (2001 - 2024)")
st.markdown("A data-driven overview of India's Electric Vehicle market using key insights and visualizations.")

# Load datasets
market_df = pd.read_csv("ev_market_overview_2024.csv")
penetration_df = pd.read_csv("ev_penetration_fy2023_24.csv")
oem_df = pd.read_csv("top_ev_oems_2024.csv")

# Section 1: Market Overview
st.header("📈 Overall EV Market Overview")
col1, col2 = st.columns(2)

with col1:
    st.subheader("EV Sales Growth")
    fig1 = px.line(market_df, x="Year", y="EV Sales", title="EV Sales in India (2001–2024)", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Market Share (%)")
    fig2 = px.bar(market_df, x="Year", y="Market Share %", title="EV Market Share in India")
    st.plotly_chart(fig2, use_container_width=True)

# Section 2: Penetration by Segment
st.header("🚗 EV Penetration by Segment (FY 2023–24)")
fig3 = px.bar(penetration_df, x="Segment", y="Penetration (%)", color="Segment",
              title="EV Penetration by Vehicle Type", text="Penetration (%)")
st.plotly_chart(fig3, use_container_width=True)

# Section 3: Top OEMs
st.header("🏭 Top Electric Two-Wheeler OEMs in 2024")
fig4 = px.pie(oem_df, names="OEM", values="Sales", title="Market Share of Top 2W OEMs")
st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown("---")
st.caption("📊 Data visualized with Streamlit and Plotly | Project by [Your Name]")
