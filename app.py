import streamlit as st
import requests
import json
import base64

GITHUB_API_ENDPOINT = "https://api.github.com/repos/{owner}/{repo}/contents/{path}"
GPT_API_ENDPOINT = "https://api.openai.com/v1/engines/davinci-codex/completions"
API_KEY = "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"

# GitHub에서 데이터를 가져오는 함수
def get_data_from_github(owner, repo, path):
    url = GITHUB_API_ENDPOINT.format(owner=owner, repo=repo, path=path)
    response = requests.get(url)
    data = response.json()
    
    # Base64로 인코딩된 데이터 디코드
    content = data["content"]
    content = content.encode("utf-8")
    content = base64.b64decode(content)
    content = content.decode("utf-8")

    return content

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
    st.title("고등학교 수학 문제 풀이 판별")

    # GitHub에서 데이터 가져오기
    owner = "your_github_username"
    repo = "your_github_repo"
    path = "data.json"
    data = get_data_from_github(owner, repo, path)
    data = json.loads(data)

    # 문제 입력
    st.header("문제 입력")
    question = st.text_area("문제를 입력하세요", height=100, value=data["question"])

    # 문제 풀이 입력
    st.header("문제 풀이 입력")
    solution = st.text_area("문제 풀이를 입력하세요", height=300, value=data["solution"])

    # 기호 지원
    st.sidebar.header("기호 지원")
    symbol = st.sidebar.selectbox("기호를 선택하세요", ("+", "-", "×", "÷", "√", "^", "sin", "cos", "tan", "log", "∫"))

    # 문제나 문제 풀이 입력란에 기호 추가
    if st.sidebar.button("기호 추가"):
        if st.text_input == question:
            question += symbol
        elif st.text_input == solution:
            solution += symbol

    # 정답 확인
    if st.button("풀이 확인"):
        # GPT 모델로 검증된 데이터 가져오기
        verified_data = get_gpt_answer(question, solution)
        verified_data = verified_data.replace("Output:", "").strip()

        # 데이터 업데이트 후 GitHub에 업데이트된 데이터 전송
        data["question"] = question
        data["solution"] = solution
        data["verified_data"] = verified_data
        updated_data = json.dumps(data)
        update_data_on_github(owner, repo, path, updated_data)

        # 검증된 데이터 출력
        st.subheader("검증된 데이터")
        st.write(verified_data)

if __name__ == "__main__":
    main()
