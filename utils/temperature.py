# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:37:23 2023

@author: MAIN
"""

import streamlit as st
import os
from PIL import Image


def app():    
    script_dir = os.path.dirname(__file__)
    pic_dict = {}
    for i in range(1,16):
        pic_dict[f't{i}'] = Image.open(script_dir + f'\\\\tem_images\\\\t{i}.png')
        
    st.header('시계열 자료 처리')
    
    st.subheader('데이터 다운로드')
    st.write('데이터는 기상청 기상자료개방포털사이트에 들어가서 받았습니다.')
    st.write('데이터란에 들어가서 종관기상관측으로 들어가서')
    st.image(pic_dict['t1'])
    st.image(pic_dict['t2'])
    st.write('위 그림의 절차를 따라 csv파일을 다운받습니다.')
    st.image(pic_dict['t3'])
    st.write('원 데이터에서 일자와 기온 열만 추출하면.')
    st.image(pic_dict['t4'])
    st.write('''
             위와 같은 89279개의 데이터를 얻을 수 있습니다. \n
             데이터의 수는 보통 31일X24시간X60분=44640처럼 짝수로 나와야하는데\n 
             89279개로 홀수가 나와 빠진 날짜가 있나 확인을 해봤습니다.
             ''')
        
    st.subheader('결측값 확인')
    st.write('하루단위로 resample을 해서 60개가 안 되는 곳이 있는지 확인해봤습니다.')             
    st.image(pic_dict['t5'])
    st.write('그 중에서도 어느 시간이 빠졌는지 보고 NaN값으로 넣어주면')
    st.image(pic_dict['t6'])
    st.image(pic_dict['t7'])
    st.write('위와 같이 잘 채워진 것을 볼 수 있습니다.')
    
    st.subheader('QC단계')
    st.write('QC단계를 통해 결측이나 오류를 찾아내어 NaN값으로 바꿔줍니다.')
    st.write('''
             QC단계는 총 4단계로 이루어집니다. \n
                 1. 결측검사 : 결측 자료를 NaN값으로 채워 넣습니다. \n
                 2. 물리 한계 검사 : 관측한 기온이 -33도 이하이거나 40도 이상으면 오류로 처리합니다. \n
                 3. 단계검사 : 현재기온과 1분전 기온이 3도이상 차이가 나면 오류로 처리합니다. \n
                 4. 지속성검사 : 단계검사에서 산출한 값의 절대값을 사용하여 시간별로 60개씩 합한 값을 구하고 합계 한 값이 0.1보다 작으면 60개 전부 오류로 처리합니다. \n
             위 데이터로 QC단계를 진행한 결과''')
    st.image(pic_dict['t8'])
    st.write('''
             **결측검사**는 아까 빠졌던 1개의 데이터이고 \n
             **물리 한계검사**와 **단계검사**상 오류는 없고 \n
             **지속성검사**상 47개의 오류발견 즉 2820의 데이터 오류를 발견하여 NaN값으로 대체해주었습니다. \n
             이를 그래프 상으로 확인한다면
             ''')
    st.image(pic_dict['t9'])
    st.write('위와 같이 지속성검사에만 오류가 발생한다는 것을 한 눈에 알 수 있습니다.')
    
    st.subheader('단위별 평균값')
    st.write('단위별로 리샘플링 했을 때 자료의 수가 80%미만이면 NaN값으로 처리하여 분석하였습니다.')
    st.write('**1시간 평균값**')
    st.write('1시간 단위로 평균값을 구한 뒤 분석을 해보았습니다.')
    st.image(pic_dict['t10'])
    st.write('결측값들로 군데군데 비어있는것을 확인 할 수 있습니다.')    

    st.write('**3시간 평균값**')
    st.write('다음으로 3시간 단위로 평균값을 구한 뒤 분석을 해보았습니다.')
    st.image(pic_dict['t11'])
    st.write('1시간평균일 때와 비교해보면 그래프의 형태는 크게 차이가 나지 않지만 결측값이 더 많은 것을 알 수 있습니다.')

    st.write('**8시간 평균값**')
    st.write('다음으로 8시간 단위로 평균값을 구한 뒤 분석을 해보았습니다.')
    st.image(pic_dict['t12'])
    st.write('3시간평균일 때와 비교해보면 그래프 형태가 좀 더 간결해지고 결측값이 더 많은 것을 알 수 있습니다.')

    st.write('**1일 평균값**')
    st.write('마지막으로 1일 단위로 평균값을 구한 뒤 분석을 해보았습니다.')
    st.image(pic_dict['t13'])
    st.write('다른 때와는 달리 결측값이 없고 그래프가 단순하게 나타나는 것을 알 수 있습니다.')
    
    st.subheader('결측치 보간하기')
    st.write('''
             위 데이터 중 3시간 평균값 데이터에 \n
             1차, 2차, 3차 보간법을 사용하여 결측치를 보간해봤습니다.''')
    st.image(pic_dict['t14'])
    st.write('보기 편하도록 7/14~7/24까지의 데이터만 이용하였습니다.')
    st.image(pic_dict['t15'])
    st.write('2차, 3차로 보간된 그래프는 비슷하고 1차로 보간된 그래프는 조금 다르다는 것을 볼 수 있습니다.')