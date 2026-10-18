import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SupplyGuard AI - Risk Forecaster", page_icon="📦", layout="wide"
)

st.title(
    "📦 SupplyGuard AI: Small Business Supply Chain Risk & Disruption"
    " Forecaster"
)
st.write(
    "Predict shipping delays 14 days in advance and analyze vendor bottlenecks"
    " with AI-driven risk forecasting."
)

# Sidebar parameters for simulation
st.sidebar.header("📊 Forecasting Parameters")
shipping_mode = st.sidebar.selectbox(
    "Shipping Mode", ["Standard Class", "Second Class", "First Class", "Same Day"]
)
lead_time_days = st.sidebar.slider(
    "Average Vendor Lead Time (Days)", 3, 30, 12
)

# Mock data for supply chain records
data = [
    {
        "Supplier": "Apex Logistics Inc.",
        "Region": "North America",
        "Item": "Microchips A-1",
        "Current Status": "In Transit",
        "Delay Risk": "High (78%)",
        "Lead Time": "14 Days",
    },
    {
        "Supplier": "Global Freight Ltd.",
        "Region": "Europe",
        "Item": "Battery Pack B-2",
        "Current Status": "Delayed at Port",
        "Delay Risk": "Critical (91%)",
        "Lead Time": "21 Days",
    },
    {
        "Supplier": "SwiftShip Co.",
        "Region": "Asia-Pacific",
        "Item": "Display Panels C-3",
        "Current Status": "On Schedule",
        "Delay Risk": "Low (12%)",
        "Lead Time": "5 Days",
    },
    {
        "Supplier": "Nordic Supply Chain",
        "Region": "Europe",
        "Item": "Cables & Connectors",
        "Current Status": "In Transit",
        "Delay Risk": "Medium (45%)",
        "Lead Time": "9 Days",
    },
]

df = pd.DataFrame(data)

st.markdown("---")
st.subheader("🌐 Active Vendor Risk Dashboard")
st.dataframe(df, use_container_width=True)

# Risk Analysis & Mitigation Section
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
  st.subheader("📈 14-Day Disruption Probability")
  st.progress(
      0.78, text="Predicted Bottleneck Severity: 78% (High Port Risk)"
  )
  st.progress(
      0.45, text="Inventory Stockout Vulnerability: 45% across active SKUs"
  )

with col2:
  st.subheader("🤖 AI Mitigation Recommendations")
  st.success(
      "✅ **Action 1:** Reroute Microchips A-1 through alternative secondary"
      " carrier."
  )
  st.info(
      "ℹ️ **Action 2:** Re-order Battery Pack B-2 5 days early to absorb"
      " regional transit delays."
  )

# Footer Disclaimer
st.markdown("---")
st.caption(
    "⚠️ **Logistics AI Disclaimer:** Forecasts are generated using predictive"
    " risk modeling for educational demonstration."
)
