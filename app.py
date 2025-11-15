import streamlit as st
import random

# 제목
st.title("랜덤 숫자 맞추기 게임! 🎮")

# 랜덤 숫자 설정 (1부터 100까지)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# 사용자가 입력할 숫자
user_guess = st.number_input("1부터 100까지 숫자를 맞춰보세요!", min_value=1, max_value=100)

# 버튼 클릭 시
if st.button("정답 확인"):
    st.session_state.attempts += 1
    
    # 숫자 맞추기
    if user_guess < st.session_state.number:
        st.write("너무 낮아요! 더 높은 숫자를 시도해보세요.")
    elif user_guess > st.session_state.number:
        st.write("너무 높아요! 더 낮은 숫자를 시도해보세요.")
    else:
        st.success(f"정답! 🎉 {st.session_state.number}를 {st.session_state.attempts}번 만에 맞췄어요!")
        st.session_state.number = random.randint(1, 100)  # 새로운 숫자 설정
        st.session_state.attempts = 0  # 시도 횟수 초기화

# 시도 횟수
st.write(f"시도 횟수: {st.session_state.attempts}번")

