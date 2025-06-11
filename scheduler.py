from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_digest  # This function must exist in main.py

def schedule_digest():
    scheduler = BlockingScheduler()
    scheduler.add_job(run_digest, 'cron', hour=21, minute=35)  # Runs every day at 9:00 AM
    print("📅 Scheduler started. Digest will run daily at 9:35 PM.")
    scheduler.start()

if __name__ == "__main__":
    schedule_digest()