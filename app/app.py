import streamlit as st

st.set_page_config(
    page_title="Admission Enquiry Chatbot",
    page_icon="🎓"
)

st.title("🎓 Admission Enquiry Chatbot")

st.write(
    "Ask questions about courses, fees, "
    "eligibility, documents and deadlines."
)

question = st.chat_input(
    "Ask your question..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        st.write(
            "This is a practice response. "
            "The RAG system will be connected later."
        )
