import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

encodingKey = "ZiLUX%2Bgd1UZWVK6xgqsuh3r7VVxBd33bdidKHPB9pJ2MuoEVMGjgAGms0G4g6PGmLFyVqGhUNP6wivLVImW9hA%3D%3D"
url = "http://apis.data.go.kr/1741000/HeatWaveShelter2/getHeatWaveShelterList2?"
params = {'ServiceKey': encodingKey, 'year': '2023'}

response = requests.get(url, params=params)

# API 요청이 성공한 경우에만 처리합니다
if response.status_code == 200:
    content = response.text

    # XML 데이터를 파싱합니다
    soup = BeautifulSoup(content, 'xml')

    rows = soup.find_all('row')

    shelter_counts = {
        "경기": 0,
        "서울": 0,
        "인천": 0,
        "강원": 0,
        "충청남": 0,
        "충청북": 0,
        "대전": 0,
        "경상북": 0,
        "경상남": 0,
        "전라북": 0,
        "전라남": 0,
        "대구": 0,
        "울산": 0,
        "부산": 0,
        "광주": 0,
        "제주": 0
    }

    shelter_good = {
        "경기": 0,
        "서울": 0,
        "인천": 0,
        "강원": 0,
        "충청남": 0,
        "충청북": 0,
        "대전": 0,
        "경상북": 0,
        "경상남": 0,
        "전라북": 0,
        "전라남": 0,
        "대구": 0,
        "울산": 0,
        "부산": 0,
        "광주": 0,
        "제주": 0
    }

    # 광역시, 도별 쉼터 개수 계산 및 조건에 맞는 쉼터 저장
    for row in rows:
        area_nm = row.find('areaNm').text
        ar = int(row.find('ar').text)
        colr_hold_arcndtn = int(row.find('colrHoldArcndtn').text)

        for area in shelter_counts.keys():
            if area in area_nm:
                if colr_hold_arcndtn == 0:
                    break
                if ar / colr_hold_arcndtn >= 50:
                    shelter_good[area] += 1
                shelter_counts[area] += 1
                break

    # Streamlit app
    st.title("지역별 무더위 쉼터 차트")

    plt.rcParams['font.family'] = 'Malgun Gothic'

    # Create buttons
    if st.button("지역별 무더위 쉼터 갯수"):
        # Display chart for shelter counts
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.bar(shelter_counts.keys(), shelter_counts.values())
        plt.xlabel("지역명")
        plt.ylabel("갯수")
        plt.title("지역별 무더위 쉼터")
        st.pyplot(plt)

    if st.button("지역별 에어컨이 갖춰진 쉼터 갯수"):
        # Display chart for good shelters
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.bar(shelter_good.keys(), shelter_good.values())
        plt.xlabel("지역명")
        plt.ylabel("갯수")
        plt.title("지역별 에어컨이 갖춰진 쉼터")
        st.pyplot(plt)

else:
    st.error("API 요청 실패: " + str(response.status_code))
