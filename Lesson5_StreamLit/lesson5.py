import streamlit as st
import time
st.set_page_config(page_title="Testing",
                   page_icon=':innocent:',
                   layout="centered",
                   initial_sidebar_state="collapsed")
with st.sidebar:
    st.title('sidebar cute')
    st.write('sidebar ko cute')
    drink = st.text_input('Ban muon uong gi')
    if st.button('menu'):
        st.write(drink)

col1, col2, col3 = st.columns(3)
with col1:
    st.header('An owl')
    st.write('Cú')
with col2:
    st.header('A dog')
    st.write('Dog')
with col3:
    st.header('A cat')
    st.write('Cat')

col4, col5, col6 = st.columns([3,3,1])
with col4:
    st.header('An owl')
    st.write('Cú')
with col5:
    st.header('A dog')
    st.write('Dog')
with col6:
    st.header('A cat')
    st.write('Cat')

with st.expander('favorite drinks'):
    st.text_input('drink name')
    st.title('Xin chào :grinning:')
    name = st.text_input('Bạn thật xấu xa, hãy nhập tên:')
    if st.button('submit name'):
        st.write(f'Hello {name}')
    dob = st.text_input('Bạn sinh ngày mấy vị ta?')
    st.write(f'Ngày sinh của bạn là {dob} phại ko')

    if st.button('balloon'):
        st.balloons()

    my_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        my_bar.progress(i + 1)



