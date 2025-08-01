import streamlit as st
import streamlit.components.v1 as htmlviewer
import re
import base64
import os

# ✅ 1. base64 변환 함수 정의 (맨 위에 복붙)
def replace_img_with_base64(html_str: str, base_dir: str = ".") -> str:
    """
    HTML 내 <img src="...">를 base64로 자동 치환
    """
    def encode_image(match):
        img_path = match.group(1)
        full_path = os.path.join(base_dir, img_path.replace("./", "").replace("\\", "/"))
        if not os.path.exists(full_path):
            print(f"❗ 이미지 없음: {full_path}")
            return match.group(0)
        with open(full_path, "rb") as f:
            img_data = f.read()
        ext = os.path.splitext(full_path)[-1].lower().replace(".", "")
        mime = f"image/{'jpeg' if ext in ['jpg', 'jpeg'] else ext}"
        encoded = base64.b64encode(img_data).decode('utf-8')
        return f'src="data:{mime};base64,{encoded}"'

    return re.sub(r'src=["\'](.*?)["\']', encode_image, html_str)

# ✅ 2. 페이지 설정 및 제목
st.set_page_config(layout='wide', page_title='CT App')
st.title('This is Boksun Webapp!!')

# ✅ 3. HTML 파일 불러오기
with open('./ct1.html', 'r', encoding='utf-8') as f:
    html1_raw = f.read()
with open('./ct2.html', 'r', encoding='utf-8') as f:
    html2_raw = f.read()
with open('./AI+ct.html', 'r', encoding='utf-8') as f:
    html3_raw = f.read()

# ✅ 4. base64로 이미지 경로 변환
html1 = replace_img_with_base64(html1_raw, base_dir='.')
html2 = replace_img_with_base64(html2_raw, base_dir='.')
html3 = replace_img_with_base64(html3_raw, base_dir='.')

# ✅ 5. 레이아웃 구성
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)

    with st.expander('Image content...'):
        st.image('./images/gpt.png')
        
    with st.expander('Content #2...'):
        htmlviewer.html(html1, height=800)

    with st.expander('Content #3...'):
        htmlviewer.html(html2, height=800)

    with st.expander('Content #4...'):
        htmlviewer.html(html3, height=800)
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)
