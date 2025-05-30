
from config import Config
from flask import Blueprint, render_template
import sqlite3

main = Blueprint('main', __name__)

@main.route('/shopping_list')
def shopping_list():
    """Render the shopping list page with items from the database."""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT product_name, quantity_to_buy FROM shopping_list")
    items = cur.fetchall()
    conn.close()
    print(f"Fetched items: {items}")
    return render_template('shopping_list.html', items=items)
