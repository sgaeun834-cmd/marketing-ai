import streamlit as st

st.set_page_config(page_title="광고 카피 레시피", layout="wide")
st.title("🎯 광고 카피 프롬프트 생성기")
st.caption("비용 없이 프롬프트를 복사해서 ChatGPT에 붙여넣으세요!")

# 입력 창
col1, col2 = st.columns(2)
with col1:
    keyword = st.text_input("핵심 키워드", placeholder="예: 항암 가발")
    target = st.text_input("타겟", placeholder="예: 40대 여성")
with col2:
    goal = st.selectbox("광 - 목적", ["전환(구매) 중심", "클릭 유도", "브랜드 인지도"])
    style = st.selectbox("문구 스타일", ["감성형", "직설형(가격)", "문제해결형"])

# 프롬프트 조합 로직
final_prompt = f"""
너는 10년차 퍼포먼스 마케터야. 아래 조건으로 광고 카피를 짜줘.

1. 키워드: {keyword}
2. 타겟: {target}
3. 목적: {goal}
4. 스타일: {style}

[요청사항]
- 네이버 파워링크 제목 10개 (15자 이내)
- 파워링크 설명 5개 (45자 이내)
- GFA 배너 카피 5개
- 각 문구는 클릭률(CTR)을 높일 수 있는 강력한 후킹 문구를 포함할 것.
"""

st.markdown("---")
st.subheader("📋 생성된 프롬프트")
st.info("아래 내용을 복사해서 ChatGPT나 클로드에 붙여넣으세요!")

# 복사하기 편하게 텍스트 박스로 출력
st.text_area("Copy & Paste", value=final_prompt, height=300)

st.success("위 내용을 복사(Ctrl+C)해서 사용하세요!")
