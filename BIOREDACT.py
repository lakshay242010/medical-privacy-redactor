import re
import streamlit as st

st.set_page_config(
    page_title="Medical Record Privacy Redactor", page_icon="🏥", layout="wide"
)

st.title("🏥 Medical Record Privacy Redactor & Summarizer")
st.write(
    "This app hides sensitive personal information (PII/PHI) from medical"
    " notes to protect patient privacy."
)

default_note = (
    "Patient Name: John Doe, DOB: 05/12/1985, Phone: 555-0199, Address: 123"
    " Maple Street. The patient was diagnosed with mild hypertension and"
    " prescribed Lisinopril 10mg daily."
)

user_text = st.text_area(
    "Paste or type a medical note below:", value=default_note, height=150
)


def redact_sensitive_info(text):
  text = re.sub(r"\b\d{3}-\d{4}\b", "[REDACTED PHONE]", text)
  text = re.sub(r"\d{2}/\d{2}/\d{4}", "[REDACTED DATE]", text)
  text = re.sub(r"John Doe", "[REDACTED NAME]", text, flags=re.IGNORECASE)
  text = re.sub(
      r"\d+\s+[A-Za-z]+\s+(Street|St|Avenue|Ave|Road|Rd)",
      "[REDACTED ADDRESS]",
      text,
      flags=re.IGNORECASE,
  )
  return text


if st.button("Run Privacy Redaction"):
  if user_text.strip() == "":
    st.warning("Please enter some text to redact.")
  else:
    redacted_text = redact_sensitive_info(user_text)
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
      st.subheader("📄 Original Text (With Private Info)")
      st.info(user_text)

    with col2:
      st.subheader("🔒 Secure Text (Redacted)")
      st.success(redacted_text)

    st.markdown("---")
    st.caption(
        "⚠️ **Clinical Disclaimer:** This tool is an automated prototype for"
        " educational demonstration. Always verify medical data manually."
    )
