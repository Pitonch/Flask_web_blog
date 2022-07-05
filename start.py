from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)
app.config['SECRET_KEY'] = '\zdjsgjsdfjcxgggjmethwergxqewxf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

from views.posts import posts_bp
app.register_blueprint(posts_bp)


if __name__ == '__main__':

    # from views.posts_orm import posts
    # app.register_blueprint(posts)

    app.run(host='0.0.0.0', port=8000)