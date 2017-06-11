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
        public_tweets = self.api.search("$ATI")
        tweetlist = [tweet.text+"<br>" for tweet in public_tweets]
        return tweetlist
        