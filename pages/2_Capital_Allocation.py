import streamlit as st

st.title("💰 Capital Allocation")

st.subheader("Capital Deployment Index")

st.metric(
    "CDI",
    "71"
)

st.write("""
### What is CDI?

Capital Deployment Index measures whether fresh money should be deployed into markets.

### Interpretation

80+ = Deploy Aggressively

60-80 = Normal Deployment

40-60 = Partial Deployment

Below 40 = Defensive
""")

st.divider()

st.subheader("Equity Deployment Score")

st.metric(
    "EDS",
    "74"
)

st.write("""
Measures attractiveness of equities.

Uses:

• Market Health
• Breadth
• Liquidity
• Sentiment
""")

st.divider()

st.subheader("Lump Sum Opportunity Score")

st.metric(
    "LOS",
    "58"
)

st.write("""
Measures whether a large one-time investment is attractive.

Higher scores indicate better lump sum opportunities.
""")

st.divider()

st.subheader("Stocks vs Mutual Funds")

st.metric(
    "Stock Selection Score",
    "68"
)

st.write("""
Current View:

Balanced

Direct stocks and mutual funds are both attractive.
""")

st.divider()

st.subheader("Today's Capital Allocation")

st.success("""
Recommended Allocation

Equity: 70%

Debt: 25%

Gold: 5%

Preferred Equity:

• Flexicap Funds
• Selected Direct Stocks

Risk Level:

Moderate
""")
