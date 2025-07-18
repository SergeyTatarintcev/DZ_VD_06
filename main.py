from app import app, db

# создаём таблицы, если их ещё нет
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)