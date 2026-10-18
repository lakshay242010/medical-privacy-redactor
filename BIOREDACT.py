import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SprintSync AI - Multi-Agent Manager", page_icon="🤖", layout="wide"
)

st.title("🤖 SprintSync AI: Multiplayer AI Sprint & Architecture Manager")
st.write(
    "A collaborative multi-agent dashboard where autonomous agents parse"
    " chats, manage task tickets, and resolve technical conflicts."
)

# Sidebar inputs for team simulation
st.sidebar.header("🛠️ Sprint Control Panel")
team_role = st.sidebar.selectbox(
    "Active Agent Persona",
    ["PM Agent (Product)", "QA Agent (Quality)", "Architect Agent (Tech)"],
)
sprint_input = st.sidebar.text_area(
    "Paste Meeting Notes / Chat Log:",
    "Need to build user login by Tuesday. Also fix database connection bug"
    " reported by QA.",
)

# Active sprint tasks data
tasks_data = [
    {
        "Task ID": "TSK-101",
        "Description": "Implement OAuth2 Login flow",
        "Priority": "High",
        "Assigned Agent": "Architect Agent",
        "Status": "In Progress",
    },
    {
        "Task ID": "TSK-102",
        "Description": "Fix DB timeout error on high load",
        "Priority": "Critical",
        "Assigned Agent": "QA Agent",
        "Status": "Conflict Flagged",
    },
    {
        "Task ID": "TSK-103",
        "Description": "Update API documentation",
        "Priority": "Medium",
        "Assigned Agent": "PM Agent",
        "Status": "Pending",
    },
]

df = pd.DataFrame(tasks_data)

st.markdown("---")
st.subheader("📋 Active Sprint Task Board")
st.dataframe(df, use_container_width=True)

# Multi-Agent Event Stream & Conflict Resolution
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
  st.subheader("⚡ Multi-Agent Event Stream")
  st.info("🤖 **PM Agent:** Parsed 3 new action items from chat logs.")
  st.success("🤖 **Architect Agent:** Verified database schema compatibility.")
  st.warning(
      "🤖 **QA Agent:** Flagged overlapping requirement in TSK-102 and"
      " TSK-104."
  )

with col2:
  st.subheader("🚨 Automated Conflict Resolution")
  st.error(
      "⚠️ **Conflict Detected:** Task TSK-102 contradicts authentication"
      " constraints in PRD section 4.2."
  )
  if st.button("Resolve Conflict via AI Agent"):
    st.success(
        "✅ Conflict automatically resolved: Updated PRD specs and"
        " reprioritized task."
    )

# Footer Disclaimer
st.markdown("---")
st.caption(
    "⚠️ **AI Dev Tool Disclaimer:** Simulated multi-agent coordination"
    " platform for educational demonstration."
)
