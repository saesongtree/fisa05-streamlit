import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

#텍스트 받고 실제로 매칭되는 사진 출력

input_text = st.text_input("찾을 그림 입력")

for i in len(ani_list):
    if input_text in ani_list[i]:
        st.image(img_list[i])