import streamlit as st

# 제목
st.title("Hello Streamlit!")

# 텍스트 출력
st.write("이것은 Streamlit의 기본 예제입니다 😊")

# 숫자 입력 받기
number = st.number_input("숫자를 입력하세요:", min_value=0, max_value=100, value=10)

st.write("입력한 숫자:", number)

# 버튼
if st.button("버튼 클릭"):
    st.success("버튼이 눌렸습니다!")
