import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼
button = st.button('버튼을 눌러봐')

if button:
    st.write(':blue[버튼]이 눌렸어 :sparkles:')

# 파일 다운로드 버튼
dataframe = pd.DataFrame(
    {
        'first column' : [1,2,3,4],
        'second column' : [10,20,30,40]
    }
)

st.download_button(
    label = 'CSV로 다운로드',
    data = dataframe.to_csv(),
    file_name = 'sample.csv',
    mime = 'text/csv'
)

# 체크박스
agree = st.checkbox('동의하십니까?')

if agree:
    st.write('동의해주셔서 감사합니다')

# 라디오 버튼
mbti = st.radio(
    '당신의 mbti는 무엇입니까?',
    ('ISTJ','ENFP','INFJ','ESTJ','선택지없음')
)

if mbti == 'ISTJ':
    st.write('논리있는척 오지네')
elif mbti == 'ENFP':
    st.write('어우 정신없어')
elif mbti == 'INFJ':
    st.write('공상주의자')
elif mbti == 'ESTJ':
    st.write('최고의 mbti')
else:
    st.write('좀 골라라 임마')

# 선택박스
mbti = st.selectbox(
    '당신의 mbti는 무엇입니까?',
    ('ISTJ','ENFP','INFJ','ESTJ','선택지없음'),
    index = 3
)

if mbti == 'ISTJ':
    st.write('논리있는척 오지네')
elif mbti == 'ENFP':
    st.write('어우 정신없어')
elif mbti == 'INFJ':
    st.write('공상주의자')
elif mbti == 'ESTJ':
    st.write('최고의 mbti')
else:
    st.write('좀 골라라 임마')

# 다중선택 박스
options = st.multiselect(
    '당신이 좋아하는 과일은 뭐야?',
    ['수박','복숭아','키위','파인애플'],
    ['복숭아']
)

# 슬라이더
# 1. 범위지정
range = st.slider(
    '범위의 값을 다음과 같이 지정할 수 있어요 :sparkles:',
    0.0, 100.0, (25.0, 75.0)
)
st.write('선택범위 : ', range)



# 2. 단일값 지정
start_time = st.slider(
    '언제 약속을 잡는 것이 좋을까?',
    min_value = dt(2025, 7, 24, 18, 0),
    max_value = dt(2025, 7, 31, 18, 0),
    value = dt(2025, 7, 26, 18, 0),
    step = datetime.timedelta(hours=1),
    format = 'YY/MM/DD - HH:mm'
)

st.write('선택된 약속 시간 : ', start_time)

# 텍스트 입력
title = st.text_input(
    '가고싶은 여행지가 있나요?',
    placeholder = '여행 도시를 입력해 줘'
)

st.write(f'네가 여행하고 싶은 도시 : :violet[{title}]')

# 숫자 입력
number = st.number_input(
    '나이를 입력해주세요.',
    min_value = 10,
    max_value = 100,
    value = 30,
    step = 5
)

st.write('당신이 입력한 나이 : ', number)