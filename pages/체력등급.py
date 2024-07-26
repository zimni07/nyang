import streamlit as st

# 데이터 준비
data = {
    '남자': {
        '100m 달리기': [(13.0, 10), (13.1, 9), (13.6, 8), (14.1, 7), (14.6, 6), (15.1, 5), (15.6, 4), (16.6, 3), (17.0, 2), (17.0, 1)],
        '1,000m 달리기': [(230, 10), (237, 9), (243, 8), (249, 7), (255, 6), (261, 5), (267, 4), (273, 3), (279, 2), (279, 1)],
        '윗몸일으키기': [(58, 10), (57, 9), (54, 8), (51, 7), (45, 6), (39, 5), (35, 4), (30, 3), (24, 2), (24, 1)],
        '좌우 악력': [(61, 10), (57, 9), (56, 8), (54, 7), (51, 6), (47, 5), (45, 4), (42, 3), (36, 2), (36, 1)],
        '팔굽혀펴기': [(58, 10), (57, 9), (52, 8), (46, 7), (40, 6), (34, 5), (29, 4), (24, 3), (18, 2), (18, 1)],
    },
    '여자': {
        '100m 달리기': [(16.5, 10), (17.1, 9), (17.6, 8), (18.1, 7), (18.6, 6), (19.1, 5), (19.6, 4), (20.1, 3), (21.1, 2), (21.1, 1)],
        '1,000m 달리기': [(290, 10), (299, 9), (305, 8), (312, 7), (319, 6), (326, 5), (332, 4), (339, 3), (346, 2), (346, 1)],
        '윗몸일으키기': [(55, 10), (54, 9), (49, 8), (45, 7), (39, 6), (34, 5), (29, 4), (24, 3), (18, 2), (18, 1)],
        '좌우 악력': [(40, 10), (39, 9), (37, 8), (35, 7), (32, 6), (29, 5), (27, 4), (26, 3), (23, 2), (23, 1)],
        '팔굽혀펴기': [(50, 10), (49, 9), (44, 8), (40, 7), (34, 6), (29, 5), (25, 4), (21, 3), (15, 2), (15, 1)],
    }
}

# 구간 데이터 변환
def get_score(event_data, input_value):
    for threshold, score in event_data:
        if input_value <= threshold:
            return score
    return 0

# 스트림릿 애플리케이션
st.title("경찰 체력 측정 점수 계산기👮👮‍♀️")

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
