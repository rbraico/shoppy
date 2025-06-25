import os
import secrets
import logging
from dotenv import load_dotenv

# Configura il logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

class Config:
    SECRET_KEY = secrets.token_hex(16)

    @staticmethod
    def get_database_path():
        db_path = os.getenv("DB_PATH")
        logger.debug(f"os.name = {os.name}")
        logger.debug(f"DB_PATH env = {db_path}")

        if db_path:
            return db_path
        else:
            raise EnvironmentError("⚠️ Variabile DB_PATH non trovata. Assicurati che .env sia presente e correttamente configurato.")

    DATABASE_PATH = get_database_path.__func__()

    @staticmethod
    def get_stockhouse_url():
        # Se è impostata la variabile d'ambiente, usala sempre (priorità massima)
        env_url = os.getenv("STOCKHOUSE_URL")
        logger.debug(f"os.name = {os.name}")
        logger.debug(f"STOCKHOUSE_URL env = {env_url}")
        if env_url:
            logger.debug(f"Uso STOCKHOUSE_URL da env: {env_url}")
            return env_url
        # Se siamo su Windows (sviluppo), usa localhost
        if os.name == "nt":
            logger.debug("Ambiente Windows rilevato, uso http://127.0.0.1:5000")
            return "http://127.0.0.1:5000"
        # Altrimenti (Home Assistant/Linux), usa l'hostname dell'add-on StockHouse
        logger.debug("Ambiente POSIX rilevato, uso http://stockhouse:9194")
        return "http://stockhouse:9194"