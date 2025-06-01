import os
import secrets


class Config:
    SECRET_KEY = secrets.token_hex(16)

    @staticmethod
    def get_database_path():
        db_path = os.getenv("DB_PATH")
        print(f"[DEBUG] os.name = {os.name}")
        print(f"[DEBUG] DB_PATH env = {db_path}")

        if db_path:
            if not os.path.exists(db_path):
                print(f"[WARNING] DB file non trovato in {db_path}. Verrà creato da SQLite se necessario.")
            else:
                print(f"[Config] DB trovato in: {db_path}")
            return db_path

        elif os.name == "nt":  # Windows
            #path = os.path.join(os.getcwd(), "sqlite_db", "stockhouse.db")
            path = r"C:\Users\Gebruiker\Projects\StockHouse\sqlite_db\stockhouse.db"
            print(f"[Config] Using Windows dev path: {path}")
            return path

        else:  # Linux/macOS/Home Assistant
            print("[Config] Using default Linux/macOS path: ./stockhouse.db")
            return "./stockhouse.db"

        
    # Inizializzazione statica
    DATABASE_PATH = get_database_path.__func__()

