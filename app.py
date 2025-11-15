import streamlit as st
import random

st.title("🎲 운명의 버튼 게임")

# 점수 초기화
if "score" not in st.session_state:
    st.session_state.score = 0

st.write(f"현재 점수: {st.session_state.score}")

# 버튼 클릭 이벤트
if st.button("누르기!"):
    event = random.choice(["point", "bomb", "money", "nothing"])
    
    if event == "point":
        st.session_state.score += 10
        st.success("🎉 점수 10점 획득!")
    elif event == "bomb":
        st.session_state.score = max(0, st.session_state.score - 20)
        st.error("💣 폭탄! 점수 20점 차감!")
    elif event == "money":
        st.session_state.score += 50
        st.success("💰 돈 획득! 점수 50점 추가!")
    else:
        st.info("😱 아무 일도 일어나지 않았습니다...")

st.write("버튼을 눌러 운명을 확인하세요!")
