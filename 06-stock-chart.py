import streamlit as st
import FinanceDataReader as Fdr
import datetime

date = st.date_input(
    '조회 시작일은 선택해봐~',
    datetime.datetime(2025,7,1)
)

code = st.text_input(
    '종목코드',
    value = '',
    placeholder = '종목코드를 입력'
)

# 해당 종목코드를 가지고 차트 그리기
if code and date:
    df = Fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)
    