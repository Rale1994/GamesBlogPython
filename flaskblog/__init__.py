from flask import Flask

from flask_sqlalchemy import SQLAlchemy  # ekstenzija za bazu
from flask_bcrypt import Bcrypt  # ekstenzija za hesiranje passworda
from flask_login import LoginManager  # ekstenizja koja nam omogucava da radimo sa login funkcinalnostima
from config import Config
from flask_mail import Mail  # eksstenzija za rad sa mejlovim konkretno za nas sto se tice resetovanje sifre

db = SQLAlchemy()  # kreiranje db insance koja se odnosi na nasu app,  #inicijalizacija ekstenzije
bcrypt = Bcrypt()  # za kriptovanje sifre, #inicijalizacija ekstenzije
login_manager = LoginManager()  # za logovanje korisnika
login_manager.login_view = 'users.login'  # da ga vrati na login stranicu ako nije ulogovan
login_manager.login_message_category = 'info'  # poruka koja upozorava da korisnik mora biti ulogovan ukoliko zeli da pristupi account stranici
mail = Mail()  # inicijalizacija ekstenzije


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from users.routes import users  # importovanje nase users putanje i  sve sto se tice users paketa

    app.register_blueprint(users)  # njeno registrovanje

    from posts.routes import posts  # importovanje nase post putanje i sve sto se tice posts paketa

    app.register_blueprint(posts)  # njeno registrovanje

    from main.routes import main  # importovanje nase main putanje  i sve sto se tice main paketa

    app.register_blueprint(main)  # njeno registrovanje

    from errors.handlers import errors  # importovanje nase errors bluprint i sve sto se tice errors paketa

    app.register_blueprint(errors)  # njeno regiistrovanje

    return app
