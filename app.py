import streamlit as st

st.set_page_config(
    page_title="IMOS Dashboard",
    layout="wide"
)

st.title("India Market Operating System (IMOS)")

st.subheader("Executive Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "IMOS Score",
        "72",
        "+2"
    )

with col2:
    st.metric(
        "Capital Deployment Index",
        "68",
        "+1"
    )

with col3:
    st.metric(
        "Debt Opportunity Score",
        "54",
        "-1"
    )
st.divider()

st.subheader("Today's Decision")

st.success("""
TODAY'S DECISION

Deploy: YES

Suggested Allocation:
70% Equity
25% Debt
5% Gold

Preferred:
Flexicap Mutual Fund

Risk Level:
Moderate
""")
