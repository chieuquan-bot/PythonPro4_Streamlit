import streamlit as st
import time
st.set_page_config(page_title="Testing",
                   page_icon=':innocent:',
                   layout="wide")
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



