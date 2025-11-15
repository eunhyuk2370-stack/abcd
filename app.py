import streamlit as st
import random

# 퀴즈 데이터 (이미지 대신 텍스트로 예시)
quiz_data = [
    {"question": "이 동물은 무엇인가요?", "image": "https://via.placeholder.com/150/FF0000/FFFFFF?text=Cat", "answer": "고양이"},
    {"question": "이 동물은 무엇인가요?", "image": "https://via.placeholder.com/150/00FF00/FFFFFF?text=Dog", "answer": "강아지"},
    {"question": "이 동물은 무엇인가요?", "image": "https://via.placeholder.com/150/0000FF/FFFFFF?text=Elephant", "answer": "코끼리"},
    {"question": "이 동물은 무엇인가요?", "image": "https://via.placeholder.com/150/FFFF00/FFFFFF?text=Lion", "answer": "사자"}
]

# 게임 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)  # 랜덤 퀴즈 선택

# 제목
st.title("퀴즈 맞추기 게임! 🎮")

# 퀴즈 불러오기
quiz = quiz_data[st.session_state.quiz_index]

# 퀴즈 질문과 이미지 표시
st.image(quiz["image"])
st.write(quiz["question"])

# 답 입력란
user_answer = st.text_input("정답을 입력하세요:")

# 정답 확인 버튼
if st.button("정답 확인"):
    if user_answer.lower() == quiz["answer"].lower():
        st.success(f"정답! 🎉")
        st.session_state.score += 1
        st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)  # 새로운 퀴즈로 변경
        st.write(f"현재 점수: {st.session_state.score}")
    else:
        st.error(f"틀렸어요! 😢 다시 도전해 보세요.")
        st.write(f"현재 점수: {st.session_state.score}")
