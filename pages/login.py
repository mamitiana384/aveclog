import streamlit as st
import json

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password

def login_page():
    st.title("🔐 Connexion")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Connexion réussie !")
            st.experimental_rerun() # Force re-run to update the view
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

# No if __name__ == "__main__": here.  main.py will call login_page()
