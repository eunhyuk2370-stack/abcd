import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("🎨 낙서 게임 – 실시간 그림판")

st.write("마우스로 아무거나 그려보세요 😎")

# 캔버스
canvas = st_canvas(
    fill_color="rgba(255, 165, 0, 0.2)",  
    stroke_width=5,
    stroke_color="#000000",
    background_color="#ffffff",
    height=400,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)

# 그린 그림 표시
if canvas.image_data is not None:
    st.image(canvas.image_data, caption="당신의 작품 🎉")

# 다운 버튼
if canvas.image_data is not None:
    st.download_button(
        "그림 다운로드",
        canvas.image_data.tobytes(),
        file_name="my_drawing.png",
        mime="image/png"
    )
