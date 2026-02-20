
import schedule
import time
from bot import TikTokEngagementBot

def job():
    bot = TikTokEngagementBot(tiktok_api)
    bot.like_video('12345')
    bot.comment_on_video('12345', 'Great video!')

def run_scheduler():
    schedule.every(1).hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    