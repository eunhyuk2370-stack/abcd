import streamlit as st
import time
import random

st.title("🦖 미니 공룡 점프 게임!")

# 초기화
if "x" not in st.session_state:
    st.session_state.x = 30  # 선인장 위치
    st.session_state.y = 0   # 공룡 높이
    st.session_state.jump = False
    st.session_state.score = 0
    st.session_state.game_over = False

# 점프 버튼
if st.button("점프! 🚀") and not st.session_state.game_over:
    if st.session_state.y == 0:
        st.session_state.jump = True

# 게임 루프
placeholder = st.empty()

while not st.session_state.game_over:
    # 점프 처리
    if st.session_state.jump:
        st.session_state.y = 1
        st.session_state.jump = False
    else:
        st.session_state.y = 0

    # 선인장 이동
    st.session_state.x -= 1
    if st.session_state.x < 0:
        st.session_state.x = 30
        st.session_state.score += 1

    # 충돌 체크
    if st.session_state.x == 5 and st.session_state.y == 0:
        st.session_state.game_over = True

    # 화면 출력
    scene = [" "] * 40
    scene[5] = "🐶" if st.session_state.y == 0 else "🐶⬆️"
    scene[st.session_state.x] = "🌵"

    placeholder.write("".join(scene))
    placeholder.write(f"점수: {st.session_state.score}")

    time.sleep(0.05)

if st.session_state.game_over:
    st.error("게임 오버! 😭 다시 실행하면 재시작됩니다.")

