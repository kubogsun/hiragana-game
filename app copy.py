import streamlit as st
# Title Msg#1
st.title('This is Boksun Webapp!!')
# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content...'):
        url = 'https://youtu.be/XyEOEBsa8I4?si=CP9z7CP6maOqTAzd'
        st.info('Content..')
        st.video(url)
    with st.expander('Content...'):
        url = 'https://youtu.be/XyEOEBsa8I4?si=CP9z7CP6maOqTAzd'
        st.info('Content..')
        st.video(url)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by Boksun Koo', unsafe_allow_html=True)
