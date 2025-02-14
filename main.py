import streamlit as st
from session import load_session_state  # Importation de la fonction pour charger l'état de la session

# Vérifier si l'utilisateur est authentifié
def check_authentication():
    session_state = load_session_state()
    if "authenticated" not in session_state or not session_state["authenticated"]:
        session_state["authenticated"] = False
    return session_state

# Page principale
def main():
    session_state = check_authentication()  # Vérifie si l'utilisateur est authentifié

    if session_state["authenticated"]:
        st.switch_page("pages/app7.py")  # Aller vers app7.py si l'utilisateur est authentifié
    else:
        st.switch_page("pages/login.py")  # Sinon, aller vers login.py

if __name__ == "__main__":
    main()
