# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:15:40 2023

@author: MAIN
"""

import streamlit as st
from utils import temperature as tem


def app():
    tab1, tab2= st.tabs(['class diagram' , '기온 시계열자료 분석'])


    with tab1:
        st.subheader('MultiPage 클래스 다이어그램')
        st.image('./page/diagram/MP_diagram.png')
        st.subheader('MultiPage 클래스 실행 로직')
        st.image('./page/diagram/class_diagram.png', use_column_width = True)
    
    with tab2:
        tem.app()
    
