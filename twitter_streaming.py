#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "736788994390790144-ZzTVpveH5F7mqjux2hhxCl5yccfF6RY"
access_token_secret = "tL2Mc7YAnyV9fNf8vAAFkxp45xFyoR52PaOiWW8bGo6fy"
consumer_key = "vbg4XSwqyqDoPXnz7NLH7MDAj"
consumer_secret = "LKlBUQMvYmFAPnaccdz5uDsQWZ6yQ9UMXX6HvlI3n52o1fzUWS"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter 
Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 
'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
