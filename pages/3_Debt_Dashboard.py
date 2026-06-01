import streamlit as st

st.title("🏦 Debt Dashboard")

st.subheader("Debt Opportunity Score")

st.metric(
    "DOS",
    "64"
)

st.write("""
### What is DOS?

Debt Opportunity Score measures whether debt investments are attractive relative to equities.

### Interpretation

80+ = Very Attractive

60-80 = Attractive

40-60 = Neutral

Below 40 = Less Attractive
""")

st.divider()

st.subheader("Recommended Debt Category")

st.success("""
Current Recommendation:

Long Duration Debt

Confidence:
78 / 100
""")

st.write("""
### Why?

• Government bond yields remain attractive.

• Inflation appears stable.

• RBI is expected to remain neutral or move toward easing.

• Long-duration bonds typically benefit most when yields decline.

### Risks

• Inflation rises again.

• RBI turns hawkish.

• Global yields move higher.
""")

st.divider()

st.subheader("Debt Allocation")

st.write("""
Suggested Debt Allocation

50% Long Duration

30% Corporate Bond Funds

20% Liquid Funds
""")

st.divider()

st.subheader("What does Long Duration mean?")

st.write("""
Long-duration debt funds invest in bonds with longer maturities.

They tend to perform best when interest rates fall.

They can be more volatile than short-duration funds.
""")
