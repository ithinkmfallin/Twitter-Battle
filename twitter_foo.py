#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
#Variables that contains the user credentials to access Twitter API&lt;/pre&gt;
access_token="2303020602-ZZGGTjl47qKQFrxHzjAsl2319Pn2W5RWLYz9hLo"
access_token_secret="DIAJDXdWoiuQLs2rJ9zsFa1XcAj2vLOPNB09c1Ij3rByB"
consumer_key="AJ1UNHfhZnFdDk3QOJcArmKHL"
consumer_secret="v8goB0Y8cp6eie1dXKAp2BRBfvi0WnK2zVvgNbOA5IwmTUZ2QD"
 
#This is a basic listener that just prints received tweets to stdout.
class Listener(StreamListener):
 
    def on_data(self, data):
        print data
        return True
 
    def on_error(self, status):
        print status
 
if __name__ == '__main__':
 
    #This handles Twitter authetification and the connection to Twitter Streaming API
    twitter_data = Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, twitter_data)
 
    #This line filter Twitter Streams to capture data by the keywords: 'manutd', 'barca'
    stream.filter(track=['manutd','barca'])