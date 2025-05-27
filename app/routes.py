from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, User, Habit, CheckIn
from datetime import date
from sqlalchemy import func

main = Blueprint('main', __name__)

# ----------------------------
# API ROUTES
# ----------------------------

@main.route('/users', methods=['POST'])
def register_user_api():
    data = request.json
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'message': 'User registered'})

@main.route('/habits', methods=['POST'])
def create_habit_api():
    data = request.json
    habit = Habit(
        user_id=data['user_id'],
        title=data['title'],
        description=data.get('description', ''),
        frequency=data['frequency']
    )
    db.session.add(habit)
    db.session.commit()
    return jsonify({'id': habit.id, 'message': 'Habit created'})

@main.route('/habits/<int:habit_id>/check-in', methods=['POST'])
def check_in_api(habit_id):
    checkin = CheckIn(habit_id=habit_id, date=date.today())
    db.session.add(checkin)
    db.session.commit()
    return jsonify({'message': 'Check-in recorded'})

@main.route('/habits/<int:habit_id>/stats', methods=['GET'])
def habit_stats_api(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    total_checkins = CheckIn.query.filter_by(habit_id=habit_id).count()
    return jsonify({
        'habit_id': habit.id,
        'title': habit.title,
        'total_check_ins': total_checkins
    })

# ----------------------------
# WEB ROUTES (Frontend)
# ----------------------------

@main.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('register.html')

@main.route('/user/<int:user_id>/habits', methods=['GET', 'POST'])
def habits(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        frequency = request.form['frequency']
        habit = Habit(user_id=user.id, title=title, description=description, frequency=frequency)
        db.session.add(habit)
        db.session.commit()
        return redirect(url_for('main.habits', user_id=user.id))
    habits = Habit.query.filter_by(user_id=user.id).all()
    return render_template('habits.html', user=user, habits=habits)

@main.route('/habit/<int:habit_id>/check-in', methods=['POST'])
def checkin_web(habit_id):
    db.session.add(CheckIn(habit_id=habit_id, date=date.today()))
    db.session.commit()
    return redirect(request.referrer or url_for('main.home'))

@main.route('/habit/<int:habit_id>/stats')
def habit_stats_web(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    total_checkins = CheckIn.query.filter_by(habit_id=habit_id).count()
    return render_template('habit_stats.html', habit=habit, total_checkins=total_checkins)
