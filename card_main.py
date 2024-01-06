import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
 

 
# 눈 내리는 애니메이션 실행
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")
 
########################################################
# Streamlit app
########################################################
# 웹앱의 페이지 세팅
st.set_page_config(page_title="Happy New Year", page_icon="🎄")
 
# 눈 내리는 애니메이션 실행
run_snow_animation()
 
# 상대방의 이름 가져오기
st.header(f"Happy New Year! 🎄🎄🎄", anchor=False)
 
# 로띠 애니메이션 실행
st_lottie("https://lottie.host/6b3e2d26-14d7-414f-829f-ab2fd97c2b04/zkKY3piuls.json")
 
 
# 메시지 출력
st.markdown(
    f"새해에는 즐겁고 행복한 일이 가득하기를 소원합니다. 🌟"
)