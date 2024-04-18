# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:29:07 2023

@author: MAIN
"""

import streamlit as st

def app():
    
    st.subheader('교통량 및 통행속도에 따른 요일별 교통체증 정도')
    
    st.write('\n')
    st.write('\n')
    
    st.write('''
             **조장 : 정은주**\n
                 - streamlit 클래스 diagram제작
                 - 요일별 교통량/통행속도 분석
                 - PPT제작 및 발표 ''')
    st.write('\n')
    st.write('''
             **조원1 : 강예진**\n
                 - 기온 시계열자료 처리
                 - 시간대별 통행속도 분석
                 - 권역별 통행속도 분석
                 - streamlit 표출 ''')
    st.write('\n')
    st.write('''
             **조원2 : 임성균**\n
                 - 기획안 작성
                 - 프로젝트 diagram제작
                 - 시간대별 교통량 분석''')