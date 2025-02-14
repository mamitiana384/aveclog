import streamlit as st
import json
from session import save_session_state  # Sauvegarde de l'état de session

# Appliquer un style CSS moderne avec effet Neumorphism
st.markdown("""
    <style>
        /* Fond sombre */
        body {
            background-color: #1e1e2e;
            color: white;
        }

        /* Conteneur du formulaire */
        .login-container {
            max-width: 350px;
            margin: auto;
            padding: 25px;
            background: #2b2b3a;
            border-radius: 15px;
            box-shadow: 8px 8px 15px #1a1a27, -8px -8px 15px #323245;
            text-align: center;
        }

        /* Titre */
        .login-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #fff;
        }

        /* Champs de texte */
        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 10px;
            border: none;
            background: #252538;
            color: white;
            font-size: 16px;
            box-shadow: inset 4px 4px 10px #1a1a27, inset -4px -4px 10px #323245;
        }

        /* Effet focus */
        input:focus {
            outline: none;
            box-shadow: 0 0 10px rgba(98, 0, 238, 0.6);
        }

        /* Bouton stylisé */
        .login-button {
            background: #6200ee;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            transition: 0.3s;
            box-shadow: 4px 4px 10px #1a1a27, -4px -4px 10px #323245;
        }

        .login-button:hover {
            background: #7f39fb;
            transform: scale(1.05);
        }

        /* Messages d'erreur */
        .stAlert {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Fonction pour charger les utilisateurs depuis un fichier JSON
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Fonction d'authentification
def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password

# Interface de connexion
def login_page():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🔐 Connexion</div>', unsafe_allow_html=True)

    username = st.text_input("👤 Nom d'utilisateur", placeholder="Entrez votre nom")
    password = st.text_input("🔑 Mot de passe", type="password", placeholder="••••••••")

    if st.button("Se connecter", key="login", help="Cliquez pour vous connecter"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("✅ Connexion réussie !")

            # Sauvegarde de l'état de la session
            save_session_state({"authenticated": True, "username": username})

            # Redirection vers app7.py
            st.switch_page("pages/app7.py")  
        else:
            st.error("🚨 Nom d'utilisateur ou mot de passe incorrect.")

    st.markdown('</div>', unsafe_allow_html=True)  # Ferme la div login-container

if __name__ == "__main__":
    login_page()
