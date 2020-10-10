import os


class Config:
    SECRET_KEY = 'fa2a37269057475efe6cfd4881b22760'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///games.db'  # za bazu
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
