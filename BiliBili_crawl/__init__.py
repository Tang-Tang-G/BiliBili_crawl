from flask import Flask


def create_app():
    app = Flask(__name__)
    from .views import account
    app.register_blueprint(account.ac)

    return app
