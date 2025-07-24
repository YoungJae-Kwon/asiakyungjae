import streamlit as st
import pandas as pd
import numpy as np

st.title('데이터 프레임 튜토리얼')

# 데이터프레임 생성
dataframe = pd.DataFrame(
    {
        'first column' : [1,2,3,4],
        'second column' : [10,20,30,40]
    }
)

st.dataframe(dataframe, use_container_width=True)

# 테이블 생성
st.table(dataframe)

# 매트릭
st.metric(label='온도', value='10°C', delta='1.2°C')
st.metric(label='삼성전자', value='80,500원', delta='-1,200원')

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label='온도', value='10°C', delta='1.2°C')
col2.metric(label='삼성전자', value='80,500원', delta='-1,200원')
col3.metric(label='달러USD', value='1,500원', delta='-1,200원')