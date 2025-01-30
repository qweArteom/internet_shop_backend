import os

from flask import Flask
from dotenv import load_dotenv

from src.database.models import db
from src.data import parse_data


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
db.init_app(app)


with app.app_context():
    db.create_all()
    parse_data.get_products()
