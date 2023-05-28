import streamlit as st
import requests

def get_weather(location):
    # 기상청 API 호출
    api_url = f'https://www.weather.go.kr/weather/observation/currentweather.jsp?auto_man=m&stn={location}'
    response = requests.get(api_url)

    if response.status_code == 200:
        # API 응답 처리
        weather_data = response.text
        # 날씨 정보 파싱 및 추천 로직 구현
        recommend_clothing(weather_data)
        recommend_items(weather_data)
    else:
        st.error("날씨 정보를 가져오는데 실패했습니다.")

def recommend_clothing(weather_data):
    # 날씨 정보에 따라 옷을 추천하는 로직을 구현
    # 예시로 간단히 추천 메시지 출력
    st.write("옷 추천: 편한 반팔과 반바지를 입으세요.")

def recommend_items(weather_data):
    # 날씨 정보에 따라 필요한 물건을 추천하는 로직을 구현
    # 예시로 간단히 추천 메시지 출력
    st.write("필요한 물건 추천: 모자와 선크림을 챙기세요.")

# Streamlit 앱 설정
st.title("날씨 옷과 물건 추천")
location = st.text_input("지역을 입력하세요")
submit_button = st.button("추천")

# 사용자 입력을 받아서 날씨 정보를 조회하고 옷과 필요한 물건을 추천합니다.
if submit_button:
    get_weather(location)
