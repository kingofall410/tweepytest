'''
Created on Jun 11, 2017

@author: Dan
'''
import tweepy

class TweepyTalk:
    '''
    classdocs
    '''
    def __init__(self):
        auth = tweepy.OAuthHandler("MeqDEn9qQHiEwxVYrxqCuyKN3",
                                   "Qs0U4bE0MAwaHzUnnIToJaGD8vZXDgGBnWk3YFVzEhhwZX6rkP")
        auth.set_access_token("511102160-jbpPv2D80opXfzwnVcLGdbbMQfTLz2JUmtUiR2RU", 
                              "hr9G44vzRHJeiCodTRtUGpDC5Zdz1LL3hYwqecqLDhTi1")
        
        self.api = tweepy.API(auth)
     
    def getTweets(self):
        public_tweets = self.api.search(geocode="39.994683,-75.311799,0.5mi", since_id="2017-06-01", rpp=100)
        tweetlist = [tweet.user.name+" - "+tweet.text+" "+str(tweet.created_at)+"<br>" for tweet in public_tweets]
        return tweetlist
        