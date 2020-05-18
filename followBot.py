#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import tweepy
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(follower.name)
            follower.follow()

def main():
    api = create_api()
    follow_followers(api)


if __name__ == "__main__":
    main()
