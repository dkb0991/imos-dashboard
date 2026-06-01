import streamlit as st
import pandas as pd

st.title("🔄 Sector Rotation")

data = {
    "Rank": [1, 2, 3, 4, 5, 6],
    "Sector": [
        "Capital Goods",
        "Defence",
        "PSU Banks",
        "Financials",
        "Pharma",
        "IT"
    ],
    "Trend": [
        "Improving",
        "Improving",
        "Stable",
        "Stable",
        "Neutral",
        "Weakening"
    ]
}

df = pd.DataFrame(data)

st.subheader("Sector Leadership Ranking")

st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Current Recommendation")

st.success("""
Preferred Sectors

1. Capital Goods

2. Defence

3. PSU Banks

Confidence:
79 / 100
""")

st.write("""
### Why?

• Strong earnings momentum

• Positive relative strength

• Institutional participation

• Government spending tailwinds

### Risks

• Valuations becoming expensive

• Rotation into defensive sectors
""")

st.divider()

st.subheader("How To Use This Page")

st.write("""
This page helps identify where new equity money should be deployed.

Higher ranked sectors should receive greater attention during stock screening.

Lower ranked sectors may still contain opportunities but are currently lagging market leadership.
""")
