from flask import Flask

from app.views import Main
from app.views import Page
from app.views import Post
from app.views import Posts
from app.misc_views import error_404
from app.misc_views import error_500
from app.misc_views import health
from app.helpers import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/cache.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.add_url_rule('/', view_func=Main.as_view('home'))
    app.add_url_rule('/<string:page>', view_func=Page.as_view('page'))
    app.add_url_rule('/post/<string:post>', view_func=Post.as_view('post'))  
    app.add_url_rule('/posts', view_func=Posts.as_view('posts'))
    app.add_url_rule('/health', view_func=health)
    app.register_error_handler(404, error_404)
    app.register_error_handler(500, error_500)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app

