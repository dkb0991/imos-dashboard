import streamlit as st

st.title("Market Intelligence")

st.subheader("Structural Health")

st.metric(
    "Structural Health Score",
    "78"
)

st.write("""
### What is it?

Measures whether the market is healthy beneath the surface.

### Why does it matter?

Strong bull markets require broad participation.

### Interpretation

80+ = Strong

60-80 = Healthy

40-60 = Neutral

Below 40 = Weak
""")

st.divider()

st.subheader("Liquidity")

st.metric(
    "Liquidity Score",
    "72"
)

st.write("""
Tracks:

- FII Flows
- DII Flows
- SIP Inflows

Why it matters:

Liquidity is one of the strongest drivers of market direction.
""")
st.divider()

st.subheader("Risk Appetite")

st.metric(
    "Risk Appetite Score",
    "75"
)

st.write("""
Measures whether investors are preferring:

• Midcaps
• Smallcaps
• PSU Banks
• Realty

Higher scores indicate a risk-on environment.
""")

st.divider()

st.subheader("Momentum")

st.metric(
    "Momentum Score",
    "69"
)

st.write("""
Tracks trend strength over:

• 1 Month
• 3 Month
• 6 Month

Strong momentum often supports higher prices.
""")

st.divider()

st.subheader("Sentiment")

st.metric(
    "Sentiment Score",
    "63"
)

st.write("""
Measures investor psychology.

Uses:

• India VIX
• Market Breadth
• Fear & Greed Conditions
""")

st.divider()

st.subheader("Crash Risk")

st.metric(
    "Crash Risk Score",
    "42"
)

st.write("""
Measures probability of a meaningful correction.

Current Status:

Moderate Risk

Not a market-timing signal.
A risk-management signal.
""")
