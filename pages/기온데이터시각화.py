import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
file_path = '/mnt/data/daily_temp.csv'
data = pd.read_csv(file_path)

# 열 이름에서 공백과 탭 제거
data.columns = data.columns.str.strip()

# 날짜를 datetime 형식으로 변환
data['날짜'] = pd.to_datetime(data['날짜'].str.strip(), format='\t%Y-%m-%d')

# 연도 추출
data['연도'] = data['날짜'].dt.year

# 연도별 기온 통계 계산
yearly_stats = data.groupby('연도').agg({
    '평균기온(℃)': 'mean',
    '최저기온(℃)': 'min',
    '최고기온(℃)': 'max'
}).reset_index()

# 스트림릿 제목
st.title("연도별 평균, 최저, 최고 기온 변화 추이")

# 그래프 선택 옵션
chart_type = st.selectbox("그래프 유형 선택", ["꺾은선 그래프", "막대 그래프"])

# 그래프 그리기
fig, ax = plt.subplots()

if chart_type == "꺾은선 그래프":
    ax.plot(yearly_stats['연도'], yearly_stats['평균기온(℃)'], label='평균 기온', marker='o')
    ax.plot(yearly_stats['연도'], yearly_stats['최저기온(℃)'], label='최저 기온', marker='o')
    ax.plot(yearly_stats['연도'], yearly_stats['최고기온(℃)'], label='최고 기온', marker='o')
    ax.set_title('연도별 평균, 최저, 최고 기온 (꺾은선 그래프)')
elif chart_type == "막대 그래프":
    bar_width = 0.25
    years = yearly_stats['연도']
    ax.bar(years - bar_width, yearly_stats['평균기온(℃)'], width=bar_width, label='평균 기온')
    ax.bar(years, yearly_stats['최저기온(℃)'], width=bar_width, label='최저 기온')
    ax.bar(years + bar_width, yearly_stats['최고기온(℃)'], width=bar_width, label='최고 기온')
    ax.set_title('연도별 평균, 최저, 최고 기온 (막대 그래프)')

ax.set_xlabel('연도')
ax.set_ylabel('기온 (°C)')
ax.legend()

# 스트림릿에 그래프 표시
st.pyplot(fig)
