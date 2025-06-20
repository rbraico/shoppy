
from config import Config
from flask import Blueprint, render_template
import sqlite3
from datetime import datetime, timedelta, date
from flask import request, jsonify
import json
import requests
        
main = Blueprint('main', __name__)



# Funzione per calcolare il numero della decade corrente
def get_current_decade(today=None):
    today = today or datetime.today()
    day = today.day
    if day <= 10:
        return "D1"
    elif day <= 20:
        return "D2"
    else:
        return "D3"

@main.route('/shopping_list')
def shopping_list():
    """Render the shopping list page with items from the database."""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cur = conn.cursor()
    decade = get_current_decade()
    cur.execute(
         "SELECT product_name, quantity_to_buy, price, shop FROM shopping_list WHERE decade_number = ?",
         (decade,)
    )
    items = cur.fetchall()
    conn.close()
    print(f"Fetched items: {items}")
    return render_template('shopping_list.html', items=items)




@main.route('/add_to_queue', methods=['POST'])
def add_to_queue():
    data = request.get_json()
    print("[DEBUG] Ricevuto dalla coda:", data)

    if not data:
        return jsonify({"status": "error", "message": "No data"}), 400

    try:
        conn = sqlite3.connect(Config.DATABASE_PATH)
        cursor = conn.cursor()

        # Estrai solo la data da timestamp ISO
        timestamp_full = data.get("timestamp")
        only_date = timestamp_full.split("T")[0] if timestamp_full else datetime.today().strftime("%Y-%m-%d")

        cursor.execute("""
            INSERT INTO shopping_queue (product_name, quantity, price, expiry, shop, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.get("product_name"),
            data.get("quantity"),
            data.get("price"),
            data.get("expiry"),
            data.get("shop"),
            only_date
        ))

        conn.commit()
        conn.close()
        print("[INFO] Prodotto inserito in shopping_queue")

    except Exception as e:
        print(f"[ERROR] Inserimento fallito: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

    # Avvisa StockHouse
    try:
        print("[DEBUG] Notifico StockHouse...")
        response = requests.post(f"{Config.get_stockhouse_url()}/trigger_queue_check", timeout=3)
        print("[INFO] StockHouse notificato, status:", response.status_code)
    except Exception as e:
        print(f"[WARNING] Impossibile contattare StockHouse: {e}")

    return jsonify({"status": "ok"})