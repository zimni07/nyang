import streamlit as st

# 데이터 준비
data = {
    '남자': {
        '100m 달리기(초)': [(13.0, float('inf'), 10), (13.1, 13.5, 9), (13.6, 14.0, 8), (14.1, 14.5, 7), (14.6, 15.0, 6), (15.1, 15.5, 5), (15.6, 16.5, 4), (16.6, 16.9, 3), (17.0, float('inf'), 1)],
        '1,000m 달리기(초)': [(0, 230, 10), (231, 237, 9), (238, 243, 8), (244, 249, 7), (250, 255, 6), (256, 261, 5), (262, 267, 4), (268, 273, 3), (274, 278, 2), (279, float('inf'), 1)],
        '윗몸일으키기(회/1분)': [(58, float('inf'), 10), (57, 57, 9), (54, 56, 8), (51, 53, 7), (45, 50, 6), (39, 44, 5), (35, 38, 4), (30, 34, 3), (24, 29, 2), (0, 23, 1)],
        '좌우 악력'(kg): [(61, float('inf'), 10), (57, 60, 9), (56, 56, 8), (54, 55, 7), (51, 53, 6), (47, 50, 5), (45, 46, 4), (42, 44, 3), (36, 41, 2), (0, 35, 1)],
        '팔굽혀펴기(회/1분)': [(58, float('inf'), 10), (57, 57, 9), (52, 56, 8), (46, 51, 7), (40, 45, 6), (34, 39, 5), (29, 33, 4), (24, 28, 3), (18, 23, 2), (0, 17, 1)],
    },
    '여자': {
        '100m 달리기': [(16.5, float('inf'), 10), (17.1, 17.0, 9), (17.6, 17.5, 8), (18.1, 18.0, 7), (18.6, 18.5, 6), (19.1, 19.0, 5), (19.6, 19.5, 4), (20.1, 20.0, 3), (21.1, float('inf'), 1)],
        '1,000m 달리기': [(0, 290, 10), (291, 299, 9), (300, 305, 8), (306, 312, 7), (313, 319, 6), (320, 326, 5), (327, 332, 4), (333, 339, 3), (340, 345, 2), (346, float('inf'), 1)],
        '윗몸일으키기': [(55, float('inf'), 10), (54, 54, 9), (49, 53, 8), (45, 48, 7), (39, 44, 6), (34, 38, 5), (29, 33, 4), (24, 28, 3), (18, 23, 2), (0, 17, 1)],
        '좌우 악력': [(40, float('inf'), 10), (39, 39, 9), (37, 38, 8), (35, 36, 7), (32, 34, 6), (29, 31, 5), (27, 28, 4), (26, 25, 3), (23, 22, 2), (0, 21, 1)],
        '팔굽혀펴기': [(50, float('inf'), 10), (49, 49, 9), (44, 48, 8), (40, 43, 7), (34, 39, 6), (29, 33, 5), (25, 28, 4), (21, 24, 3), (15, 20, 2), (0, 14, 1)],
    }
}

# 구간 데이터 변환 함수
def get_score(event_data, input_value):
    for lower, upper, score in event_data:
        if lower <= input_value <= upper:
            return score
    return 0

# 스트림릿 애플리케이션
st.title("경찰공무원 체력 측정 점수 계산기👮‍♀️👮")

# 성별 선택
gender = st.selectbox("성별을 선택하세요", list(data.keys()))

# 종목별 기록 입력
scores = {}
for event in data[gender]:
    score = st.number_input(f"{event} 기록을 입력하세요", min_value=0.0, format="%.1f")
    scores[event] = score

# 점수 계산
total_score = 0
for event, score in scores.items():
    total_score += get_score(data[gender][event], score)

# 결과 출력
st.write(f"총점: {total_score}")
