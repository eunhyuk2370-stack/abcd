import streamlit as st
import random

st.title("⚡ 숫자 피하기 스피드 게임")

# 점수 초기화
if "score" not in st.session_state:
    st.session_state.score = 0

# 랜덤 숫자 생성
danger_num = random.randint(1, 20)
st.write(f"⚠️ 위험 숫자: {danger_num}")

# 플레이어 입력
player_num = st.number_input("1~20 숫자를 입력하세요 (위험 숫자 피하기!)", min_value=1, max_value=20, step=1)

if st.button("입력"):
    if player_num == danger_num:
        st.session_state.score = max(0, st.session_state.score - 5)
        st.error("💥 위험! 점수 5점 차감")
    else:
        st.session_state.score += 1
        st.success("✅ 안전! 점수 +1")
    
    st.write(f"현재 점수: {st.session_state.score}")
