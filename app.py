# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:20:24 2023

@author: Jung
"""

import streamlit as st
from multipage import MultiPage
from page import intro, class_tem, project_diagram, project_outline, traffic
from page import project_insight, project_improve

app = MultiPage()

st.title('주간프로젝트 1조')

app.add_page('소개', intro.app)
app.add_page('프로젝트 개요', project_outline.app)
app.add_page('프로젝트 개발기술 고도화', class_tem.app)
app.add_page('프로젝트 Diagram', project_diagram.app)
app.add_page('분석내용', traffic.app)
app.add_page('인사이트 도출', project_insight.app)
app.add_page('개선사항', project_improve.app)

app.run()