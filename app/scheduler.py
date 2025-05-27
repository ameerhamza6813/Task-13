from apscheduler.schedulers.background import BackgroundScheduler
from .models import db, User, Habit, CheckIn, ReportLog
from flask import current_app
from datetime import date, timedelta
import os
import sendgrid
from sendgrid.helpers.mail import Mail

def send_weekly_reports():
    with current_app.app_context():
        users = User.query.all()
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)

        for user in users:
            habits = Habit.query.filter_by(user_id=user.id).all()
            report = f"Weekly Report for {user.name}\n\n"
            for habit in habits:
                count = CheckIn.query.filter(
                    CheckIn.habit_id == habit.id,
                    CheckIn.date >= week_start,
                    CheckIn.date <= week_end
                ).count()
                report += f"{habit.title}: {count} check-ins\n"

            # Send email
            sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
            message = Mail(
                from_email=os.getenv('FROM_EMAIL'),
                to_emails=user.email,
                subject='Your Weekly Habit Tracker Report',
                plain_text_content=report
            )
            sg.send(message)

            # Log report generation
            log = ReportLog(user_id=user.id, week_start=week_start)
            db.session.add(log)
        db.session.commit()

def init_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_weekly_reports, trigger='cron', day_of_week='sun', hour=0)
    scheduler.start()
