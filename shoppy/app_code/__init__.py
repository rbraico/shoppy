from flask import Flask

def create_app():
    try:
        app = Flask(__name__, static_url_path='/static', static_folder='static')
        app.config.from_object('config.Config')

        from .routes import main
        app.register_blueprint(main)

        return app

    except Exception as e:
        import traceback
        print("💥 ECCEZIONE IN create_app:")
        traceback.print_exc()
        raise

