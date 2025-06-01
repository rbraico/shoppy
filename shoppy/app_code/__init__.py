from flask import Flask

def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')
    app.config.from_object('config.Config')

    from .routes import main
    app.register_blueprint(main)

    return app
