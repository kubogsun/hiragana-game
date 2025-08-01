import streamlit as st
import streamlit.components.v1 as htmlviewer
# Title Msg#1
st.set_page_config(layout='wide', page_title='CT App')
st.title('This is Boksun Webapp!!')

with open('./ct1.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
    f.close()

with open('./ct2.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
    f.close()

with open('./AI+ct.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
    f.close()

# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)

    with st.expander('Image content...'):
        imgfilepath = './images/gpt.png'
        st.image(imgfilepath)
        
    with st.expander('Content #2...'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html1, height=800)
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)
