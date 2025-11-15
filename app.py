import streamlit as st
import random

st.title("🎲 운명의 버튼 – 업그레이드 버전")

# 게임 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "items" not in st.session_state:
    st.session_state.items = []

st.write(f"현재 점수: {st.session_state.score}")
st.write(f"아이템: {', '.join(st.session_state.items) if st.session_state.items else '없음'}")

# 버튼 클릭 이벤트
if st.button("운명의 버튼 누르기!"):
    events = [
        {"desc": "🎉 점수 10점 획득!", "score": 10, "item": None},
        {"desc": "💣 폭탄! 점수 20점 차감!", "score": -20, "item": None},
        {"desc": "💰 돈 획득! 점수 50점 추가!", "score": 50, "item": None},
        {"desc": "😱 아무 일도 안 일어남...", "score": 0, "item": None},
        {"desc": "🛡️ 방패 획득! 다음 폭탄 피해", "score": 0, "item": "방패"},
        {"desc": "🔥 점수 2배 버프!", "score": 0, "item": "점수2배"},
        {"desc": "🍀 행운! 추가 점수 30점!", "score": 30, "item": None},
        {"desc": "💀 치명타! 점수 50점 차감!", "score": -50, "item": None},
        {"desc": "✨ 마법 아이템 획득!", "score": 0, "item": "마법"},
        {"desc": "🎁 랜덤 보상! 점수 20~100점!", "score": random.randint(20, 100), "item": None}
    ]
    
    event = random.choice(events)
    
    # 방패 아이템 체크
    if event["score"] < 0 and "방패" in st.session_state.items:
        st.warning("🛡️ 방패로 폭탄 피해! 점수 차감 없음!")
        st.session_state.items.remove("방패")
    else:
        st.session_state.score += event["score"]
    
    # 아이템 획득
    if event["item"]:
        st.session_state.items.append(event["item"])
    
    st.write(event["desc"])
    st.write(f"현재 점수: {st.session_state.score}")
    st.write(f"아이템: {', '.join(st.session_state.items) if st.session_state.items else '없음'}")

