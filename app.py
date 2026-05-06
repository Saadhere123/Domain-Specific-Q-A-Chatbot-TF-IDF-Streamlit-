import streamlit as st
from chatbot import TFIDFChatbot


bot = TFIDFChatbot("qa_dataset.csv")

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("AI Q&A Chatbot ")
st.write("Ask questions related to AI, programming, or technology.")

if "history" not in st.session_state:
    st.session_state.history = []


user_input = st.text_input("You:", placeholder="Type your question here...")

col1, col2 = st.columns([1,1])

with col1:
    ask_btn = st.button("Ask")

with col2:
    clear_btn = st.button("Clear Chat")


if clear_btn:
    st.session_state.history = []


if ask_btn and user_input:
    matched_q, answer, score = bot.get_response(user_input)

    if answer is None:
        st.session_state.history.append({
            "user": user_input,
            "matched": "No match found",
            "answer": "Sorry, I don't understand.",
            "score": score
        })
    else:
        st.session_state.history.append({
            "user": user_input,
            "matched": matched_q,
            "answer": answer,
            "score": score
        })

for chat in reversed(st.session_state.history):
    st.markdown(f"**🧑 You:** {chat['user']}")
    st.markdown(f"**🔍 Matched Question:** {chat['matched']}")
    st.markdown(f"**🤖 Bot:** {chat['answer']}")
    st.markdown(f"**📊 Confidence:** {chat['score']:.2f}")
    st.markdown("---")