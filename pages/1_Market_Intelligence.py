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
