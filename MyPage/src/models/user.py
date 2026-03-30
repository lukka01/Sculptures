from MyPage.src.ext import db
from MyPage.src.models.base import BaseModel

class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True, nullable = False)
    password = db.Column(db.String(64), unique = True, nullable = False)
    age = db.Column(db.Integer, nullable = False)