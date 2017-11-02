import tweepy
import time
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import Stream

C_KEY = 'TR4gOd7J3cA5qCpWAMPj9Y9ls'
C_SECRET = 'QbqygSH6yR5heLvXhgZSomZPDRhJUowYEWfskj14G3lJ03EFJv'
A_TOKEN_KEY = '908444306867998720-p0yN6CSH2oM5xmVX2qxrW12vX03VLBP'
A_TOKEN_SECRET = 'ZOv9Doo3DjC4oOqnGSONlEFX7DaG3AseMbveCUO3jn2Tw'

# create a StreamListener class ADAPTED from lecture notes
class MyListener(StreamListener):
    def __init__(self, time_limit=10):
        self.start_time = time.time()
        self.limit = time_limit
        self.outFile = open('bts2.json', 'w')
        super(MyListener, self).__init__()
        
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.outFile.write(data)
            self.outFile.write('\n')
            return True
        else:
            self.outFile.close()
            return False
        
    def on_error(self, status):
        print(status)

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN_KEY, A_TOKEN_SECRET)
api = tweepy.API(auth)

#myStream = Stream(auth, MyListener(time_limit=1800))
#myStream.filter(track=['BTS'])

file = open('bts2.json', 'r') 
print file.readlines() 

#with open('bts2.json') as f:
#    for line in f:
#        data.append(json.loads(line))
