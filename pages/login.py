import streamlit as st
import json
from session import save_session_state  # Importation pour sauvegarder l'état de la session

# CSS pour un design moderne
st.markdown("""
    <style>
        /* Arrière-plan avec un dégradé et effet flou */
        .main {
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Conteneur principal */
       

        /* Style du titre */
        .login-title {
            color: #fff;
            font-size: 24px;
            margin-bottom: 20px;
            font-weight: bold;
        }

        /* Style des champs */
        .stTextInput>div>div>input {
            border-radius: 8px;
            padding: 10px;
            border: 2px solid #ccc;
            width: 100%;
            transition: all 0.3s ease-in-out;
            font-size: 16px;
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #764ba2;
            outline: none;
            box-shadow: 0 0 8px rgba(118, 75, 162, 0.5);
        }

        /* Icônes à côté des champs */
        .input-container {
            position: relative;
            margin-bottom: 20px;
        }

        .input-icon {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: #764ba2;
        }

        .stTextInput input {
            padding-left: 35px;
        }

        /* Style du bouton */
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
            transition: 0.3s ease-in-out;
        }

        .login-button:hover {
            background: linear-gradient(135deg, #5563de, #5a3d91);
            transform: scale(1.05);
        }

        /* Message d'erreur centré */
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

# Page de connexion
def login_page():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    st.markdown('<div class="login-title">🔐 Connexion</div>', unsafe_allow_html=True)

    username = st.text_input("Nom d'utilisateur", placeholder="Entrez votre nom")
    password = st.text_input("Mot de passe", type="password", placeholder="••••••••")

    if st.button("Se connecter", key="login", help="Cliquez pour vous connecter", use_container_width=True):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("✅ Connexion réussie !")

            # Sauvegarder l'état de la session
            save_session_state({"authenticated": True, "username": username})

            # Rediriger vers app7.py
            st.switch_page("pages/app7.py")  
        else:
            st.error("🚨 Nom d'utilisateur ou mot de passe incorrect.")

    st.markdown('</div>', unsafe_allow_html=True)  # Ferme login-card
    st.markdown('</div>', unsafe_allow_html=True)  # Ferme main

if __name__ == "__main__":
    login_page()
