# Twitter-Bots
A repo for python twitter bots - let's automate things

## Getting Started
First you will need to create a twitter developer account to be able to access 
the Twitter API: https://developer.twitter.com/en/apply-for-access

Next you will need to set environment variables, in linux:
```
export CONSUMER_KEY="your_consumer_key"
export CONSUMER_SECRET="your_consumer_secret"
export ACCESS_TOKEN="your_access_token"
export ACCESS_TOKEN_SECRET="your_access_token_secret" 
```

Now you should be able to run any of the above using for example:
```
python3 followBot.py
```

## What bots are included?

### drawReplyUserBot.py
A Twitter bot which draws and tweets any user's profile picture after they 
have replied with a tweet containing the string "draw me" in it. Makes use of 
`drawImage.py` in the `resources` directory

### drawBot
A bot that will create and tweet a hand drawn image of your own profile picture.

### motivationBot
A bot to tweet the day of the week using the `time` module, a given quote and 
the gif `thankYou.gif` located in the `resources` directory.

### dailyBot
A bot to favourite all tweets, retweet half and follow some tweets/users based 
on a given filter ("#100DaysOfCode" by default).

### followBot
A twitter bot which follows everyone who follows me who I don't currently follow.

### favRetweetBot
A twitter bot to favourite and retweet all tweets based on a given filter.

### autoreplyBot
A twitter bot to auto replys to mentions like an answer machine.

### config.py
Contains config to connect to the Twitter API, gets values from Environment 
Variables.


## Built with

* [Tweepy](https://www.tweepy.org/) - An easy-to-use Python library for 
accessing the Twitter API.

## Acknowledgments

Thanks to the [#100DaysOfCode](https://twitter.com/search?q=%23100daysOfCode&src=hashtag_click)
 Twitter community for encouraging me to code for fun!!
 
This was my starting point and will help anyone get started with Python Twitter bots:
https://realpython.com/twitter-bot-python-tweepy/