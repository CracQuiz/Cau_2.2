import streamlit as st
import time
import webbrowser as wb

st.title('Đăng nhập')
user_name = st.text_input('Username', '')
pass_word = st.text_input('Password', '', type='password')

if st.button('Đăng nhập'):
    if user_name == '21521323' and pass_word == '21521323':
        st.success('Đăng nhập thành công')
        time.sleep(3)
        wb.open('https://www.uit.edu.vn/')
    else:
        st.error('Sai username hoặc password')
