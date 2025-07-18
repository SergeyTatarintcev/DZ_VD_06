from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    hobby = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User({self.name}, {self.city}, {self.hobby}, {self.age})"