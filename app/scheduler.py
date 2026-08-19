from apscheduler.schedulers.background import BackgroundScheduler
from app.config import settings
from app.database import SessionLocal
from app.services.post_service import create_daily_post

scheduler = BackgroundScheduler(timezone=settings.timezone)

def daily_job():
    db = SessionLocal()
    try:
        create_daily_post(db, auto_publish=settings.auto_publish)
    finally:
        db.close()

def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            daily_job,
            "cron",
            hour=settings.daily_post_hour,
            minute=settings.daily_post_minute,
            id="daily-linkedin-post",
            replace_existing=True,
        )
        scheduler.start()
