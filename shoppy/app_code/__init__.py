import os
from flask import Flask

def create_app():
    try:
        # Calcola il percorso assoluto alla cartella "static"
        base_dir = os.path.abspath(os.path.dirname(__file__))
        #static_dir = os.path.join(base_dir, '..', 'static')
        static_dir = os.path.abspath(os.path.join(base_dir, '..', '..', 'static'))
        # Inizializza l'app Flask con percorso static personalizzato
        app = Flask(__name__, static_url_path='/static', static_folder=static_dir)
        app.config.from_object('config.Config')

        from .routes import main
        app.register_blueprint(main)

        return app

    except Exception as e:
        import traceback
        print(".... ECCEZIONE IN create_app:")
        traceback.print_exc()
        raise
