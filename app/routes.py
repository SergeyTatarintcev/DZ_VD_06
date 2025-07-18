from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # извлекаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if name and city and hobby and age:
            # создаём объект и сохраняем в БД
            user = User(name=name, city=city, hobby=hobby, age=int(age))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    users = User.query.all()  # получаем всех пользователей
    return render_template('form.html', users=users)