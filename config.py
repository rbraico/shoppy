import os
import secrets
from dotenv import load_dotenv

# Carica il file .env (automaticamente dalla root del progetto)
load_dotenv()

class Config:
    SECRET_KEY = secrets.token_hex(16)

    @staticmethod
    def get_database_path():
        db_path = os.getenv("DB_PATH")
        print(f"[DEBUG] os.name = {os.name}")
        print(f"[DEBUG] DB_PATH env = {db_path}")

        if db_path:
            return db_path
        else:
            raise EnvironmentError("⚠️ Variabile DB_PATH non trovata. Assicurati che .env sia presente e correttamente configurato.")

    DATABASE_PATH = get_database_path.__func__()

    @staticmethod
    def get_stockhouse_url():
        return os.getenv("STOCKHOUSE_URL", "http://127.0.0.1:5000")
