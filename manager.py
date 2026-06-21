import streamlit as st

from database import create_tables
from auth import *
from pages.employee import employee_dashboard
from pages.manager import manager_dashboard

st.set_page_config(
    page_title="Leave Management",
    page_icon="📅",
    layout="wide"
)

create_tables()

with open(
    "assets/style.css"
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

st.markdown("""
<div class='main-header'>
<h1>📅 Leave Management System</h1>
<p>Employee & Manager Self-Service Portal</p>
</div>
""", unsafe_allow_html=True)

if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Login",
            "Register"
        ]
    )

    if menu == "Register":

        st.subheader(
            "Create Account"
        )

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            [
                "Employee",
                "Manager"
            ]
        )

        if st.button(
            "Register"
        ):

            if register_user(
                username,
                password,
                role
            ):

                st.success(
                    "Registration Successful"
                )

            else:

                st.error(
                    "User Exists"
                )

    else:

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Login"
        ):

            user = login_user(
                username,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.username = user[1]
                st.session_state.role = user[3]

                st.rerun()

            else:

                st.error(
                    "Invalid Credentials"
                )

else:

    st.sidebar.success(
        st.session_state.username
    )

    st.sidebar.info(
        st.session_state.role
    )

    if st.sidebar.button(
        "Logout"
    ):

        st.session_state.clear()
        st.rerun()

    if st.session_state.role == "Employee":
        employee_dashboard()

    else:
        manager_dashboard()