import streamlit as st

st.set_page_config(
    page_title="IMOS Dashboard",
    layout="wide"
)

st.title("🇮🇳 IMOS - Investment Decision System")

st.subheader("Executive Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "IMOS Score",
        "Loading..."
    )

with col2:
    st.metric(
        "Capital Deployment Index",
        "Loading..."
    )

with col3:
    st.metric(
        "Debt Opportunity Score",
        "Loading..."
    )

st.divider()

st.subheader("Today's Decision")

st.info("""
Waiting for live market data...
""")
