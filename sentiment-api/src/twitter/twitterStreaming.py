from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="dmTjNTJcZKvOwYNoygfYygSWV"
csecret="XAhVtgm4gNMUlDAbEfLdbetFVY6DU1gVc319eEWFvmIAmtX0kl"
atoken="2828139721-BiMIpykRJL3AVWvOjZcglMVw3QNC2qyzPz96BA8"
asecret="yLawWAHmLdvgVeck2okdsykDBMtCBTbfTs569u00aL4cX"


class listener(StreamListener):

    def __init__(self, queue):
        self.queue = queue

    def on_data(self, data):
        self.queue.put(data)
        return(True)

    def on_error(self, statuschannels):
        print (statuschannels)

class TwiteerStreaming:

  def filter(self, queue,location):
     auth = OAuthHandler(ckey, csecret)
     auth.set_access_token(atoken, asecret)
     twitterStream = Stream(auth, listener(queue),async=True)
     lct=[location[0]["lng"],location[0]["lat"], location[1]["lng"],location[1]["lat"]]
     print(lct)
     twitterStream.filter(locations=lct,tweet_mode="extended")