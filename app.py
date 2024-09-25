# import streamlit as st

# st.title("Welcome to sign up page")

# # with st.sidebar:
    
# name = st.text_input("Name")
# phone = st.text_input('Phone')
# DOB = st.date_input("DOB")
# email = st.text_input('Email')
# password = st.text_input("Password", type = "password")

# button = st.button("Sign Up!")

# with st.sidebar:
#     st.button("Login")
#     st.button("SignUp")

import streamlit as st
from utils import check_json, load_users

# Main function to manage navigation
def main():
    check_json()

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        st.set_page_config(page_title="Login/Signup")
        st.session_state['page'] = 'Login/Signup'
    else:
        st.set_page_config(page_title="Marks Entry")
        st.session_state['page'] = 'Marks Entry'

if __name__ == '__main__':
    main()
