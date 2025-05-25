from flask import Blueprint, render_template
import sqlite3

bp = Blueprint('main', __name__)

@bp.route('/')
def show_list():
    conn = sqlite3.connect('/percorso/al/database/stockhouse.db')
    c = conn.cursor()
    c.execute("SELECT nome_prodotto, quantita FROM shopping_list ORDER BY nome_prodotto")
    items = c.fetchall()
    conn.close()
    return render_template('shopping_list.html', items=items)
