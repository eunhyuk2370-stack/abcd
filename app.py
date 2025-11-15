import streamlit as st
import random
import time

# 게임 상태 초기화
if "game_over" not in st.session_state:
    st.session_state.game_over = False
    st.session_state.score = 0
    st.session_state.dinosaur_pos = 0  # 0은 낮음, 1은 점프 중
    st.session_state.cactus_pos = 30  # 선인장의 위치

# 제목
st.title("🦖 미니 공룡 점프 게임!")

# 점프 버튼
if st.button("점프! 🚀") and not st.session_state.game_over:
    if st.session_state.dinosaur_pos == 0:
        st.session_state.dinosaur_pos = 1  # 점프 상태로 변경

# 게임 루프 (각 프레임을 매번 갱신)
if not st.session_state.game_over:
    # 선인장 이동
    st.session_state.cactus_pos -= 1
    if st.session_state.cactus_pos < 0:
        st.session_state.cactus_pos = 30
        st.session_state.score += 1

    # 점프 상태 되돌리기 (시간 지나면)
    if st.session_state.dinosaur_pos == 1:
        time.sleep(0.2)
        st.session_state.dinosaur_pos = 0  # 점프 후 다시 낮아짐

    # 충돌 체크
    if st.session_state.cactus_pos == 5 and st.session_state.dinosaur_pos == 0:
        st.session_state.game_over = True  # 충돌하면 게임 오버

    # 화면 그리기
    scene = [" "] * 40  # 화면 크기 40칸
    scene[5] = "🐶" if st.session_state.dinosaur_pos == 0 else "🐶⬆️"  # 공룡
    scene[st.session_state.cactus_pos] = "🌵"  # 선인장
    st.write("".join(scene))
    st.write(f"점수: {

