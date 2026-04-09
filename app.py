import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="광고 마스터 AI", layout="wide")
st.title("🚀 광고 구조 & 소재 생성 AI")

with st.sidebar:
    st.header("설정")
    api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")

col1, col2 = st.columns(2)
with col1:
    keyword = st.text_input("핵심 키워드 (예: 항암 가발)")
    target = st.text_input("타겟 (예: 40대 여성)")
with col2:
    goal = st.selectbox("광고 목적", ["전환 중심", "클릭 유도", "브랜드 인지도"])
    budget = st.text_input("예산 (예: 월 100만원)")

if st.button("광고 전략 및 카피 생성하기"):
    if not api_key:
        st.error("API Key를 입력해주세요!")
    else:
        client = OpenAI(api_key=api_key)
        prompt = f"마케터로서 {keyword}, {target}, {goal}, {budget}에 맞는 광고 전략과 카피를 짜줘."
        res = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
        st.write(res.choices[0].message.content)
