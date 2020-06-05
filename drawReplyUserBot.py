#!/usr/bin/python3.8

import tweepy
import logging
from config import create_api
from resources.drawImage import drawImage
import matplotlib.pyplot as plot
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweet_image(api, tweet):
    try:
        logger.info(f"{tweet.user.name} has replied to your status, let's go!")
        tweet_message = f"Hello {tweet.user.name}, I hope you enjoy your drawing"
        
        image_path = get_profile_picture_path(api, tweet.user)
        image = drawImage(image_path)
        
        # save image to temp file
        plot.imsave('temp.png', image, cmap='gray', vmin=0, vmax=255)
        
        media_list = get_image(api)
            
        logger.info(f"replying to status: {tweet.id}")
        # send reply with drawn image of user
        api.update_status(status = tweet_message,
                          in_reply_to_status_id = tweet.id, 
                          auto_populate_reply_metadata=True,
                          media_ids=media_list)
        logger.info("Tweet sent successfully! :) ")
    except:
        logger.info("failed to draw image")
    
def get_profile_picture_path(api, user):
    
    # get url of profile picture
    image_path = user.profile_image_url_https
    
    # original image path is the above with "_normal" removed from the url
    original_image_path = image_path.replace('_normal', '')
    logger.info(f"image url: {original_image_path}")
    
    return original_image_path

def get_image(api):
    media_list = list()
    
    # read image from temp file (probably a better way to do this)
    response = api.media_upload("temp.png")
    media_list.append(response.media_id_string)
    return media_list

def check_replies(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        logger.info(f"new mention found from {tweet.user.name}...")
        new_since_id = max(tweet.id, new_since_id)
        if ("draw me" in tweet.text.lower()):
            
            logger.info(f"sending drawing...")
            tweet_image(api, tweet)

    return new_since_id

def main():
    api = create_api()
    since_id = 1 
    while True:
        since_id = check_replies(api, since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
        
    