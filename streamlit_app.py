import streamlit as st
import streamlit.components.v1 as components

secret_token = "mysecret"
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."


)


st.write(
    "below is an embedded streamlit app."


)

iframe_src = f"https://chatbot-ch4trmyyf6u.streamlit.app/?embedded=true&token={secret_token}"
components.iframe(iframe_src)