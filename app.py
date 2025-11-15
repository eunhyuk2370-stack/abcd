import streamlit as st
import random

st.title("🤣 무한 이상한 버튼")

if "responses" not in st.session_state:
    st.session_state.responses = []

funny_responses = [
    "💥 오! 갑자기 치즈가 떨어짐!",
    "🐙 문어가 등장했다!",
    "🎩 모자가 날아감!",
    "🍌 바나나 껍질에 미끄러짐!",
    "👽 외계인 등장! 안녕?",
    "🔥 방 안이 갑자기 뜨거워짐!"
]

if st.button("뭐가 일어날까?"):
    response = random.choice(funny_responses)
    st.session_state.responses.append(response)

for r in st.session_state.responses:
    st.write(r)
