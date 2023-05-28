import streamlit as st
import requests
import json

GPT_API_ENDPOINT = "https://api.openai.com/v1/engines/davinci-codex/completions"
API_KEY = "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"

# GPT API로부터 답변을 받는 함수
def get_gpt_answer(question, solution):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": f"1. 문제: {question}\n2. 문제 풀이: {solution}\n3.",
        "max_tokens": 100,
        "temperature": 0.7
    }

    response = requests.post(GPT_API_ENDPOINT, headers=headers, json=data)
    answer = response.json()["choices"][0]["text"].strip()

    return answer

# Streamlit 앱 메인 부분
def main():
    st.title("고등학교 수학 문제 풀이 검증")

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요", height=100)

    # 문제 풀이 입력
    st.header("문제 풀이 입력")
    solution = st.text_area("문제 풀이를 입력하세요", height=300)

    # 정답 확인
    if st.button("풀이 확인"):
        # GPT 모델로 검증된 데이터 가져오기
        verified_data = get_gpt_answer(question, solution)

        # 검증된 데이터 출력
        st.subheader("검증된 데이터")
        st.write(verified_data)

if __name__ == "__main__":
    main()
