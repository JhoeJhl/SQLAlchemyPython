from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tutorial.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique=True)

    def __repr__(self):
        return f"<User name='{self.name}' email='{self.email}'>"
    
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactoriamente")

if __name__ == '__main__':
    init_db()