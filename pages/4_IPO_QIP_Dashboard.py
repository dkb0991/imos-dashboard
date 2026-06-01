import streamlit as st

st.title("IPO & QIP Dashboard")

st.subheader("Capital Raising Heat Index")

st.metric(
    "CRHI",
    "68"
)

st.write("""
### What is CRHI?

Capital Raising Heat Index measures how aggressively companies are raising capital.

It combines:

• IPO Activity

• QIP Activity

• OFS Activity

• SME IPO Activity

### Interpretation

80+ = Euphoria

60-80 = Hot

40-60 = Healthy

Below 40 = Weak
""")

st.divider()

st.subheader("IPO Euphoria Index")

st.metric(
    "IPO Euphoria",
    "61"
)

st.write("""
Measures:

• IPO subscriptions

• Listing gains

• Retail participation

Current Assessment:

Optimistic but not euphoric.
""")

st.divider()

st.subheader("Promoter Confidence Index")

st.metric(
    "PCI",
    "58"
)

st.write("""
Measures:

• Promoter buying

• Promoter selling

• OFS activity

Interpretation:

Higher scores indicate stronger promoter confidence.
""")

st.divider()

st.subheader("Current IPO Market View")

st.success("""
Recommendation:

Selective Participation

Confidence:
72 / 100
""")

st.write("""
### Why?

• IPO activity remains healthy.

• QIP activity indicates companies can raise capital.

• Retail participation remains elevated but not extreme.

### Risks

• Excessive SME IPO speculation.

• Weak post-listing performance.

• Overvaluation of new listings.
""")

st.divider()

st.subheader("IPO Watchlist")

st.info("""
Future Version:

This section will automatically display:

• Upcoming IPOs

• Subscription data

• Listing gains

• AI assessment

• Participation recommendation
""")
