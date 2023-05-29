import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.rcParams["font.family"] = "Arial Unicode MS"

encodingKey = "ZiLUX%2Bgd1UZWVK6xgqsuh3r7VVxBd33bdidKHPB9pJ2MuoEVMGjgAGms0G4g6PGmLFyVqGhUNP6wivLVImW9hA%3D%3D"
url = "http://apis.data.go.kr/1741000/HeatWaveShelter2/getHeatWaveShelterList2?"
params = {'ServiceKey': encodingKey, 'year': '2023', 'type' : 'json'}


# API 요청이 성공한 경우에만 처리합니다
try:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        shelters = data['HeatWaveShelter'][1]['row']


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
        for shelter in shelters:
            area_nm = shelter['areaNm']
            ar = int(shelter['ar'])
            colr_hold_arcndtn = int(shelter['colrHoldArcndtn'])

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

        # Create buttons
        if st.button("지역별 무더위 쉼터 갯수"):
            # Display chart for shelter counts
            fig, ax = plt.subplots(figsize=(10, 6))
            plt.bar(shelter_counts.keys(), shelter_counts.values())
            plt.xlabel("지역명")
            plt.ylabel("갯수")
            plt.title("지역별 무더위 쉼터")
            plt.savefig("chart.png")

            # 이미지 출력
            st.image("chart.png")

        if st.button("지역별 에어컨이 갖춰진 쉼터 갯수"):
            # Display chart for good shelters
            fig, ax = plt.subplots(figsize=(10, 6))
            plt.bar(shelter_counts.keys(), shelter_counts.values())
            plt.xlabel("지역명")
            plt.ylabel("갯수")
            plt.title("지역별 무더위 쉼터")
            plt.savefig("chart.png")

            # 이미지 출력
            st.image("chart.png")

    else:
        st.error("API 요청 실패: " + str(response.status_code))

except requests.RequestException as e:
    st.error("API 요청 실패: " + str(e))
