from flask import render_template, request, Blueprint
from flaskblog.models import Post

main=Blueprint('main',__name__) #zadavanje imena putanja prema nasem delu aplikacije koje se tice

@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)  # obelezavanje strane od koje ce da krece
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,
                                                                  per_page=5)  # dovalacenje svih postova iz baze perko upita query.all(), kao i broj postova po strani
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
