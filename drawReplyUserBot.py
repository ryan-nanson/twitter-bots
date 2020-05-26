#!/usr/bin/python3.8

import tweepy
import logging
from config import create_api
from resources.drawImage import drawImage
import matplotlib.pyplot as plot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet_image(api):
    
    tweet_message = "Tweet message goes here!!"
    
    image_path = get_profile_picture_path(api)
    image = drawImage(image_path)
    
    # save image to temp file
    plot.imsave('temp.png', image, cmap='gray', vmin=0, vmax=255)
    
    media_list = get_image(api)
        
    # send tweet with image
    #api.update_status(status=tweet_message, media_ids=media_list)
    logger.info("Tweet sent successfully! :) ")
    
def get_profile_picture_path(api):
    user = api.me()
    
    # should we use profile_image_url or profile_image_url_https?
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

def main():
    api = create_api()
    tweet_image(api)


if __name__ == "__main__":
    main()
    
    
    