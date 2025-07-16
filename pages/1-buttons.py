import streamlit as st

a = st.button('클릭')
st.write(a)

#사진 찍으면 다운
if image := st.camera_input('Click a snap2'): #사진 찍기 전에는 들여쓰기 안 코드 반환x
    st.download_button('다운로드', image, 'my png')