#!/usr/bin/python3.8

import tweepy
import logging
from config import create_api
from datetime import date
import calendar

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet_motivation(api, day):
    logger.info("Tweeting motivation")
    
    logger.info(f"Happy {day}")
    #api.update_status(f"Happy {day}")
    
def get_day():    
    todays_date = date.today()
    today_name = calendar.day_name[todays_date.weekday()]
    logger.info(f"Today is {today_name}")
    return today_name

def main():
    api = create_api()
    day = get_day()
    tweet_motivation(api, day)


if __name__ == "__main__":
    main()
    
    
    