import streamlit as st
import yfinance as yf
from utils.score_engine import get_scores
st.set_page_config(
    page_title="IMOS Dashboard",
    layout="wide"
)
scores = get_scores()
# Live Market Data

nifty = yf.Ticker("^NSEI")
vix = yf.Ticker("^INDIAVIX")

nifty_hist = nifty.history(period="2d")
vix_hist = vix.history(period="2d")

nifty_price = "N/A"
nifty_change = "N/A"
vix_price = "N/A"

if len(nifty_hist) >= 2:
    nifty_price = round(nifty_hist["Close"].iloc[-1], 2)

    nifty_change = round(
        nifty_hist["Close"].iloc[-1]
        - nifty_hist["Close"].iloc[-2],
        2
    )

if len(vix_hist) >= 1:
    vix_price = round(vix_hist["Close"].iloc[-1], 2)
st.title("🏠 Executive Dashboard")

st.subheader("Executive Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "IMOS Score",
        scores["imos"]
    )

with col2:
    st.metric(
        "Capital Deployment Index",
        scores["cdi"]
    )

with col3:
    st.metric(
        "Debt Opportunity Score",
        scores["dos"]
    )
st.subheader("Market Snapshot")

colA, colB, colC = st.columns(3)

with colA:
    st.metric(
        "Nifty 50",
        "Coming Soon"
    )

with colB:
    st.metric(
        "India VIX",
        "Coming Soon"
    )

with colC:
    st.metric(
        "Market Status",
        "Coming Soon"
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
st.divider()

st.subheader("What is IMOS Score?")

st.write("""
The IMOS Score measures the overall health of the Indian stock market.

It combines:

- Structural Health
- Liquidity
- Risk Appetite
- Momentum
- Sentiment
- IPO/QIP Activity

Interpretation:

80-100 → Strong Bull Market

60-80 → Healthy Market

40-60 → Neutral

20-40 → Weak Market

0-20 → High Risk
""")
st.divider()

st.subheader("Current Dashboard Status")

st.write("""
✅ Deployment Working

✅ Dashboard Online

✅ Automatic Updates Enabled

🔄 Live Market Data - Coming Soon

🔄 Debt Market Signals - Coming Soon

🔄 IPO/QIP Heat Index - Coming Soon

🔄 Sector Rotation - Coming Soon
""")
