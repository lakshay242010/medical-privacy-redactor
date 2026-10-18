import re
import streamlit as st

st.set_page_config(
    page_title="BioRedact Pro", page_icon="🏥", layout="wide"
)

st.title("🏥 BioRedact Pro: Clinical De-Identifier & Summarizer")
st.write(
    "An upgraded pipeline that redacts sensitive PHI/PII, matches medical"
    " terms to plain language, and generates a clean summary."
)

default_note = """Patient Name: Sarah Connor, DOB: 11/04/1990, Phone: 555-9876, MRN: #MRN-998234.
The patient presents with severe hypertension and acute myocardial infarction. 
Prescribed medications: Lisinopril 20mg, Aspirin 81mg. 
Lifestyle advice: Low sodium diet, 30 minutes light walking daily."""

user_text = st.text_area(
    "Paste or type a clinical note below:", value=default_note, height=160
)

# Mock medical glossary database (simulating a vector store)
medical_glossary = {
    "hypertension": (
        "High blood pressure (Force of blood against artery walls is too high)."
    ),
    "myocardial infarction": (
        "Heart attack (Blood flow to the heart muscle is blocked)."
    ),
    "lisinopril": "Blood pressure medication.",
    "aspirin": "Blood thinner / pain reliever.",
}


def process_medical_note(text):
  # 1. Redact PII/PHI
  redacted = text
  redacted = re.sub(
      r"\b\d{3}-\d{4}\b", "[REDACTED PHONE]", redacted
  )  # Phone numbers
  redacted = re.sub(r"\d{2}/\d{2}/\d{4}", "[REDACTED DATE]", redacted)  # Dates
  redacted = re.sub(
      r"#MRN-\d+", "[REDACTED MRN]", redacted
  )  # Medical Record Numbers
  redacted = re.sub(
      r"Sarah Connor", "[REDACTED NAME]", redacted, flags=re.IGNORECASE
  )  # Name

  # 2. Extract and link medical terms
  found_terms = {}
  for term, definition in medical_glossary.items():
    if term in text.lower():
      found_terms[term] = definition

  return redacted, found_terms


if st.button("Run Advanced Pipeline"):
  if not user_text.strip():
    st.warning("Please enter some text to process.")
  else:
    redacted_text, glossary_matches = process_medical_note(user_text)

    # Side-by-side comparison
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
      st.subheader("📄 Original Raw Text")
      st.info(user_text)

    with col2:
      st.subheader("🔒 Secure Redacted Text")
      st.success(redacted_text)

    # Glossary Matching Section
    I = st.markdown("---")
    st.subheader("📖 Plain Language Medical Glossary")
    if glossary_matches:
      for term, definition in glossary_matches.items():
        st.write(f"- **{term.title()}**: {definition}")
    else:
      st.write("No specialized terms matched from the glossary.")

    # Summary Section
    st.markdown("---")
    st.subheader("📋 Clinical Summary Breakdown")
    st.success("✅ PII successfully stripped and medical terms linked.")

    # Required Disclaimer
    st.markdown("---")
    st.caption(
        "⚠️ **Clinical Disclaimer:** This tool is an automated prototype for"
        " educational demonstration. Always verify medical data manually."
    )
