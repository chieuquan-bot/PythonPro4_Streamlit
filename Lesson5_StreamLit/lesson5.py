import streamlit as st
import time

st.title('Web Cute :grinning:')
name = st.text_input('Bạn thật xấu xa, hãy nhập tên:')
if st.button('submit name'):
    st.write(f'Hello {name}')
dob = st.text_input('Bạn sinh ngày mấy vị ta?')
st.write(f'Ngày sinh của bạn là {dob} phại ko')

if st.button('balloon'):
    st.balloons()

if st.button('dep gai'):
    st.image('IMG_0185.JPG')

my_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    my_bar.progress(i + 1)



