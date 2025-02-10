import streamlit as st

# Si l'utilisateur est connecté, on charge l'application principale
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.switch_page("pages/app7.py")  # Vers app7.py dans le dossier 'pages'
else:
    st.switch_page("pages/login.py")  # Vers login.py dans le dossier 'pages'
