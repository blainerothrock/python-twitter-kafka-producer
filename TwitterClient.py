import twitter
import logging, os, json

class TwitterClient:

    consumer_key = os.getenv("TWITTER_CONSUMER_KEY", "")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", "")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN", "")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET", "")
    
    api = None

    def __init__(self):
        self.connect() 

    def connect(self):
        self.api = twitter.Api(consumer_key=self.consumer_key,
                  consumer_secret=self.consumer_secret,
                  access_token_key=self.access_token,
                  access_token_secret=self.access_secret)

        screenName = self.api.VerifyCredentials().screen_name
        if screenName != None:
            logging.debug(screenName + " authenicated")

    def stream(self, track):
        stream = self.api.GetStreamFilter(
            track=track
        )
        while True:
            tweet = next(stream)
            text = tweet.get("text")
            user = tweet.get("user")
            data = {}
            data["user"] = user
            data["message"] = text
            if user != None and text != None:
                yield json.dumps(data)
