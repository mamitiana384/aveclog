import streamlit as st
import json
from session import save_session_state  # Sauvegarde de l'état de session

# Appliquer un style CSS moderne avec effet Neumorphism
st.markdown("""
<style>
body {
    background-color: #f4f4f4;
    font-family: 'Arial', sans-serif; /* Police plus moderne */
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh; /* Assure le centrage vertical */
    margin: 0; /* Supprime les marges par défaut */
}

.login-container {
    background-color: white;
    padding: 40px;
    border-radius: 12px; /* Bords plus arrondis */
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); /* Ombre plus prononcée */
    width: 400px;
    transition: transform 0.3s ease, opacity 0.3s ease; /* Transitions douces */
    opacity: 0.9; /* Opacité initiale */
}

.login-container:hover {
    transform: scale(1.02); /* Légère augmentation au survol */
    opacity: 1;
}

.login-title {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
    font-weight: 600; /* Plus gras */
}

.form-group {
    margin-bottom: 20px;
}

.form-label {
    font-weight: 500;
    margin-bottom: 8px;
    color: #555;
}

.form-input {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 6px; /* Bords plus arrondis */
    box-sizing: border-box;
    transition: border-color 0.3s ease; /* Transition de la bordure */
}

.form-input:focus {
    border-color: #007bff; /* Bordure bleue au focus */
    outline: none; /* Supprime l'outline par défaut */
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.2); /* Ombre légère au focus */
}

.login-button {
    background-color: #007bff;
    color: white;
    padding: 14px 24px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    width: 100%;
    font-weight: 500;
    transition: background-color 0.3s ease, transform 0.2s ease; /* Transitions multiples */
}

.login-button:hover {
    background-color: #0056b3;
    transform: translateY(-2px); /* Légère translation vers le haut */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Ombre au survol */
}

.error-message, .success-message {
    margin-top: 15px;
    text-align: center;
    transition: opacity 0.3s ease; /* Transition pour les messages */
}

.error-message {
    color: #dc3545; /* Rouge */
}

.success-message {
    color: #28a745; /* Vert */
}

/* Animation de chargement (optionnel) */
.loader {
    border: 8px solid #f3f3f3; /* Bordure grise */
    border-top: 8px solid #007bff; /* Bordure bleue */
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 2s linear infinite; /* Animation de rotation */
    margin: 20px auto;
    display: none; /* Masqué par défaut */
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>
""", unsafe_allow_html=True)

# Fonction pour charger les utilisateurs depuis un fichier JSON
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Le fichier 'users.json' n'a pas été trouvé. Veuillez le créer.")
        return {}  # Retourne un dictionnaire vide pour éviter les erreurs

# Fonction d'authentification
def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password

# Page de connexion
def login_page():
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='login-title'> Connexion</h2>", unsafe_allow_html=True)

    username = st.text_input("Nom d'utilisateur", placeholder="Entrez votre nom d'utilisateur", key="username", label_visibility="hidden", container_width=True, autocomplete="username")
    password = st.text_input("Mot de passe", type="password", placeholder="Entrez votre mot de passe", key="password", label_visibility="hidden", container_width=True, autocomplete="current-password")

    if st.button("Se connecter", key="login_button", use_container_width=True):
        # Afficher le loader (optionnel)
        st.markdown("<div class='loader' id='loading'></div>", unsafe_allow_html=True)
        st.experimental_rerun()

        # Simuler un délai (pour montrer le loader)
        import time; time.sleep(1)  # Délai réduit à 1 seconde

        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.markdown("<p class='success-message'>Connexion réussie !</p>", unsafe_allow_html=True)
            save_session_state({"authenticated": True, "username": username})
            st.switch_page("pages/app7.py")
        else:
            st.markdown("<p class='error-message'>Nom d'utilisateur ou mot de passe incorrect.</p>", unsafe_allow_html=True)

        # Masquer le loader après l'authentification
        st.markdown("<script>document.getElementById('loading').style.display = 'none';</script>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    login_page()
