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

### motivationBot
A bot to tweet the day of the week, a given quote and a gif.

### dailyBot
A bot to favourite all tweets, retweet half and follow some tweets/users based 
on a given filter.

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