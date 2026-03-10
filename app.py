# %%
import streamlit as st
import pandas as pd
import numpy as np

# 앱 제목 설정
st.title('🚀 나의 첫 Streamlit 웹 앱')

# 간단한 텍스트 출력
st.write('GitHub를 통해 배포된 Streamlit 페이지입니다.')

# 사이드바 만들기
st.sidebar.header('설정')
name = st.sidebar.text_input('이름을 입력하세요', '방문자')

# 데이터 프레임 및 차트 생성
st.subheader(f'안녕하세요, {name}님! 실시간 차트 확인하기')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)

# 데이터 표 보여주기
if st.checkbox('데이터 표 보기'):
    st.write(chart_data)