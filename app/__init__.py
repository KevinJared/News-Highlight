from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # creating the app config
    app.config.from_object(config_options[config_name])

    # initialize flask extensions
    bootstrap.init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # set up config
    from .requests import configure_requests
    configure_requests(app)
    
    return app