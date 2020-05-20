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
    
    happy_day = f"Happy {day}! "
    message = get_motivational_quote(api)
    
    tweet_message = f"{happy_day}{message}"
    logger.info(f"{tweet_message}")
    
    media_list = get_gif(api)
    
    logger.info("Sending tweet")
    api.update_status(status=tweet_message, media_ids=media_list)
    
def get_gif(api):
    media_list = list()
    response = api.media_upload('thankyou.gif')
    return media_list.append(response.media_id_string)

def get_motivational_quote(api):
    return "Day 3 of #100DaysOfCode Thank you for helping me reach 100 followers - this tweet was written by my python bot"
    
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
    
    
    