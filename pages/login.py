import streamlit as st
import json
from session import save_session_state  # Importation pour sauvegarder l'état de la session

# CSS pour améliorer le style de la page de connexion
st.markdown("""
    <style>
        /* Centre la boîte de connexion */
        .login-container {
            max-width: 400px;
            margin: auto;
            padding: 30px;
            background: white;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
        }

        /* Style des champs */
        .stTextInput>div>div>input {
            border-radius: 8px;
            padding: 10px;
            border: 2px solid #ccc;
            transition: all 0.3s ease-in-out;
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #4f46e5;
            outline: none;
            box-shadow: 0 0 8px rgba(79, 70, 229, 0.5);
        }

        /* Style du bouton */
        .login-button {
            background: linear-gradient(135deg, #4f46e5, #9333ea);
            color: white;
            padding: 10px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            transition: 0.3s;
        }

        .login-button:hover {
            background: linear-gradient(135deg, #3b82f6, #9333ea);
            transform: scale(1.05);
        }

        /* Centrer les erreurs */
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
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.title("🔐 Connexion")

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

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    login_page()
