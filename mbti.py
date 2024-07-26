import streamlit as st

# 제목 설정
st.title('나의 MBTI 특징 알아보기!!')

# 이름 입력
name = st.text_input('이름을 입력해주세요 : ')

# MBTI 선택
mbti = st.selectbox('당신의 MBTI를 선택해주세요:', 
                    ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 
                     'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'])

# 인사말 생성 버튼
if st.button('특징 설명 및 추천'):
    if name and mbti:
        # MBTI 설명 및 추천
        mbti_descriptions = {
            'ISTJ': "ISTJ는 책임감이 강하고 신뢰할 수 있으며, 체계적이고 현실적입니다. "
                    "이들은 논리적이며, 규칙과 절차를 중시합니다. "
                    "분석적 사고를 통해 문제를 해결하고, 신중하게 의사 결정을 내립니다. "
                    "어울리는 MBTI: ESFP",

            'ISFJ': "ISFJ는 따뜻하고 친절하며, 헌신적입니다. "
                    "이들은 세심하고, 다른 사람들을 돌보는 것을 좋아합니다. "
                    "전통과 안정성을 중시하며, 자세하고 꼼꼼합니다. "
                    "어울리는 MBTI: ESTP",

            # ... 다른 MBTI 설명 추가

            'ENTJ': "ENTJ는 리더십이 강하고, 목표 지향적이며, 결단력 있습니다. "
                    "이들은 전략적 사고와 계획 수립에 능합니다. "
                    "효율성과 성과를 중시하며, 도전을 즐깁니다. "
                    "어울리는 MBTI: INTP"
        }

        description = mbti_descriptions.get(mbti, "선택한 MBTI에 대한 설명이 없습니다.")
        st.write(f'{name}님! 당신의 MBTI는 {mbti}입니다. {description}')
    else:
        st.write("이름과 MBTI를 입력해주세요.")
