import streamlit as st

# Vérifier si l'utilisateur est authentifié
def check_authentication():
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.session_state["authenticated"] = False

# Page principale
def main():
    check_authentication()

    if st.session_state["authenticated"]:
        st.switch_page("pages/app7.py")  # Aller vers app7.py si l'utilisateur est authentifié
    else:
        st.switch_page("pages/login.py")  # Sinon, aller vers login.py

if __name__ == "__main__":
    main()
