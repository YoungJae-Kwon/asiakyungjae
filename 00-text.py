import streamlit as st
st.title('이것은 타이틀입니다')
st.title('쓸어담아 :moneybag:')
st.header('헤더를 입력할 수 있을까말까')
st.header('ㅋㅋㅋㅋㅋ :smiling_imp:')
st.subheader('이곳은 서브헤더임')
st.subheader('gggggggg :heart_eyes: ')
st.caption('캡션을 넣어봤다리')

# 코드 표시
sample_code = '''
def function():
    print("안녕 파이썬!")
'''
st.code(sample_code, language='python')

# 일반 텍스트
st.text('일반적인 텍스트를 입력해 봤어')

st.markdown('streamlit은 **마크다운 문법을 지원**한다!')
st.markdown('streamlit은 :red[**마크다운 문법을 지원**]한다!')
st.markdown('텍스트의 색상은 :green[하하하]으로, 그리고 **:blue[호호호]** 볼드체로 설정가능하다.')

# 수식 지원
st.latex(r'\sqrt{x^2+y^2}=1')