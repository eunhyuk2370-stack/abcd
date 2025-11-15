import streamlit as st
import random
import time

# 게임 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# 게임 타이머
elapsed_time = time.time() - st.session_state.start_time
remaining_time = 30 - int(elapsed_time)

# 게임 종료 조건
if remaining_time <= 0:
    st.write("⏱️ 게임 시간 끝!")
    st.write(f"최종 점수: {st.session_state.score}")
    st.button("게임 재시작", on_click=lambda: reset_game())

# 풍선 클릭하면 터짐
if st.button("풍선 클릭!"):
    balloon_size = random.randint(50, 150)
    balloon_position = random.randint(1, 100)
    st.write(f"풍선 위치: {balloon_position} / 풍선 크기: {balloon_size}")
    
    st.session_state.score += balloon_size
    st.write(f"점수: {st.session_state.score}")

# 타이머 표시
st.write(f"남은 시간: {remaining_time}초")


