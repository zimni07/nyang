import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
file_path = '/mnt/data/daily_temp.csv'
data = pd.read_csv(file_path)

# 날짜를 datetime 형식으로 변환
data['date'] = pd.to_datetime(data['date'])

# 연도 추출
data['year'] = data['date'].dt.year

# 연도별 기온 통계 계산
yearly_stats = data.groupby('year')['temperature'].agg(['mean', 'min', 'max']).reset_index()

# 스트림릿 제목
st.title("연도별 평균, 최저, 최고 기온 변화 추이")

# 그래프 선택 옵션
chart_type = st.selectbox("그래프 유형 선택", ["꺾은선 그래프", "막대 그래프"])

# 그래프 그리기
fig, ax = plt.subplots()

if chart_type == "꺾은선 그래프":
    ax.plot(yearly_stats['year'], yearly_stats['mean'], label='평균 기온', marker='o')
    ax.plot(yearly_stats['year'], yearly_stats['min'], label='최저 기온', marker='o')
    ax.plot(yearly_stats['year'], yearly_stats['max'], label='최고 기온', marker='o')
    ax.set_title('연도별 평균, 최저, 최고 기온 (꺾은선 그래프)')
elif chart_type == "막대 그래프":
    ax.bar(yearly_stats['year'] - 0.2, yearly_stats['mean'], width=0.2, label='평균 기온')
    ax.bar(yearly_stats['year'], yearly_stats['min'], width=0.2, label='최저 기온')
    ax.bar(yearly_stats['year'] + 0.2, yearly_stats['max'], width=0.2, label='최고 기온')
    ax.set_title('연도별 평균, 최저, 최고 기온 (막대 그래프)')

ax.set_xlabel('연도')
ax.set_ylabel('기온 (°C)')
ax.legend()

# 스트림릿에 그래프 표시
st.pyplot(fig)
