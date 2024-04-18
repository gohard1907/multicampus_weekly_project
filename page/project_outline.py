# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:22:30 2023

@author: MAIN
"""

import streamlit as st
import os
from PIL import Image



def app():
    script_dir = os.path.dirname(__file__)
    pic_dict = {}
    for i in range(1,2):
        pic_dict[f'o{i}'] = Image.open(script_dir + f'\\\\outline\\\\o{i}.png')
    
    
    st.header('프로젝트 기획배경 및 목표')
    
    st.subheader('1. 프로젝트 배경')
    st.info('''
            많은 사람들이 월요일 출근길과 금요일 퇴근길이 유독 막힌다고 말합니다.
            소수의 사람은 사실 별 차이는 없다고 말하기도 합니다.
            이와 같은 논쟁 속에서 실제로 객관적인 데이터는 어느 쪽을 말하는지 궁금증이 생겨 분석하게 되었습니다.
            ''')            
            
            
    st.subheader('2. 사전조사')
    st.markdown("[사전조사 블로그](http://thtyle.com/blog/2013/05/monday-friday-traffic-jam/)")
    st.info('''
            오래되었지만 같은 주제의 분석이 있습니다.\n
            이에 따르면 실제 출퇴근 시간에 차량 통행량이 많고, 
            월요일이 다른 평일에 비해서 출근시간 통행량이 많은 구간이 많다는 것을 알 수 있습니다.
            ''')
    st.image(pic_dict['o1'])
    
    
    st.subheader('3. 목표')
    st.write('데이터를 통해 아래와 같은 4가지의 목표를 확인하고자 합니다.')
    st.info('''
            1. 22년도 서울시 시간대별 교통량과 통행속도를 확인하여 어느 시간대에 교통체증이 심한지 파악
            2. 22년도 서울시 요일별 도심 교통량/통행속도 확인하여 어느 요일에 교통체증이 심한지 파악
            3. 22년도 서울시 요일별 도시고속 교통량/통행속도 확인하여 어느 요일에 교통체증이 심한지 파악
            4. 22년도 서울시 권역별 통행속도 확인하여 어느 서울 권역의 교통체증이 심한지 파악            
            ''')
    