import streamlit as st

ani_list = ['짱구는못말려', '몬스터', '릭앤모티']
img_list = [
    'https://i.imgur.com/t2ewhfH.png',
    'https://i.imgur.com/ECROFMC.png',
    'https://i.imgur.com/MDKQoDc.jpg'
]

# 실시간으로 입력값 반영
query = st.text_input("애니 이름(일부) 입력:")

# 빈 입력값은 결과 없음
if query:
    # 부분 일치 필터링 (대소문자 구분 없이)
    matched = [
        (ani, img) for ani, img in zip(ani_list, img_list)
        if query.lower() in ani.lower()
    ]
    if matched:
        for ani, img_url in matched:
            st.image(img_url, caption=ani)
    else:
        st.warning("검색어와 일치하는 애니가 없습니다.")
