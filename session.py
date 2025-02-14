import pickle
import os

SESSION_FILE = "session_state.pkl"

def save_session_state(session_data):
    with open(SESSION_FILE, "wb") as f:
        pickle.dump(session_data, f)

def load_session_state():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "rb") as f:
            return pickle.load(f)
    return {}  # Retourne un dict vide si aucun fichier n'existe
