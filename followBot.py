
"""
Created on Fri May 15 15:34:34 2020

@author: ryan_joseph
@title: followBot
@description: a bot to follow anyone who follows me who I don't follow'
"""
#!/usr/bin/python3.8
import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(follower.name)
            follower.follow()

def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("EqCuMmJ0JWYaTSfYeFmjSxsaK",
                               "tdgE02hRB9sShztd5AmT4mIyDq9I5GI8q5hOxfVWkONQgJmghN")
    auth.set_access_token("1260616594209869826-cCRBJoKhegZjytpmAmSM4JPSlYT5oK",
                          "uwphMGgYgR81KWCpyNDS518uXKO2occux1y6rEhQJ16Er")

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    return api

def main():
    api = create_api()
    follow_followers(api)


if __name__ == "__main__":
    main()
