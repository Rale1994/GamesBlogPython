# funkcija koja ce da cuva izmenjenu sliku
import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import url_for
from flask import current_app
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics',
                                picture_fn)  # zadavanje putanje gde ce se cuvati uploadovana slika

    # podesavanje velicine slike koju uploadujemi
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)

    image.save(picture_path)  # na kraju cuvamo nasu sliku u picture_path koji smo u koraku pre definisali

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}
    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)