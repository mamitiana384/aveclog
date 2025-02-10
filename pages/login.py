import streamlit as st
import json

# Fonction pour charger les utilisateurs depuis un fichier JSON
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Fonction d'authentification
def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password

# Page de connexion
def login_page():
    st.title("🔐 Connexion")
    
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Connexion réussie !")

            # Rediriger vers app7.py
            st.switch_page("pages/app7.py")  
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

if __name__ == "__main__":
    login_page()
