import streamlit as st
import json
from session import save_session_state  # Fonction pour sauvegarder l'état de session

# Appliquer un style CSS moderne
st.markdown("""
    <style>
        /* Arrière-plan en dégradé */
        body {
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
        }

        /* Conteneur du formulaire */
     

        /* Titre */
        .login-title {
            font-size: 24px;
            color: #fff;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Style des champs de texte */
        input {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #ccc;
            font-size: 16px;
        }

        /* Effet focus */
        input:focus {
            border-color: #764ba2;
            outline: none;
            box-shadow: 0 0 10px rgba(118, 75, 162, 0.5);
        }

        /* Bouton stylisé */
        .login-button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            transition: 0.3s;
        }

        .login-button:hover {
            background: linear-gradient(135deg, #5563de, #5a3d91);
            transform: scale(1.05);
        }
        .login-button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            transition: 0.3s;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        }

        .login-button:hover {
            background: linear-gradient(135deg, #7b7eff, #9b5be3);
            transform: scale(1.05);
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.4);
        }

        .login-button:active {
            background: linear-gradient(135deg, #4d4dff, #6a3da0);
            transform: scale(0.98);
        }

        /* Pour aligner au centre */
        .stButton > button {
            display: block;
            margin: 0 auto;
        }
        /* Messages d'erreur centrés */
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

    if st.button("Se connecter", key="login", help="Cliquez pour vous connecter", css_class="login-button"):
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
