import streamlit as st
import yfinance as yf
from utils.score_engine import get_scores
from models.recommendation import (
    get_market_assessment,
    get_deployment_action,
    get_debt_assessment
)
from models.asset_allocation import get_asset_allocation
st.set_page_config(
    page_title="IMOS Dashboard",
    layout="wide"
)
scores = get_scores()
market_assessment = get_market_assessment(
    scores["imos"]
)

deployment_action = get_deployment_action(
    scores["cdi"]
)

debt_assessment = get_debt_assessment(
    scores["dos"]
)
allocation = get_asset_allocation(
    scores["imos"],
    scores["cdi"],
    scores["dos"]
)
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
st.success(f"""
Market Assessment: {market_assessment}

Capital Deployment: {deployment_action}

Debt Assessment: {debt_assessment}
""")
st.subheader("Fresh Capital Deployment Plan")

st.info("""
⚠️ This recommendation applies ONLY to NEW money available for investment.

⚠️ It is NOT a recommendation to sell or rebalance existing holdings.
""")

st.write(f"Equity: {allocation['Equity']}%")
st.write(f"Debt: {allocation['Debt']}%")
st.write(f"REITs: {allocation['REITs']}%")
st.write(f"Gold: {allocation['Gold']}%")
st.write(f"Cash: {allocation['Cash']}%")

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
