# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:32:34 2023

@author: MAIN
"""

import streamlit as st


class MultiPage:
    
    def __init__(self):
        self.pages=[]
        
    def add_page(self, title, func):
        self.pages.append({'title':title, 'function':func})
        
    def run(self):
        page = st.sidebar.selectbox(
            '주간프로젝트',
            self.pages,
            format_func = lambda page: page['title']
            )
        
        page['function']()