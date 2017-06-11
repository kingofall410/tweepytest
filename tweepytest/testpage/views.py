from django.shortcuts import render
from django.http import HttpResponse

from tweepytest.tweepytalk import TweepyTalk
from tweepy import Status
# Create your views here.

def test(request):
    tt = TweepyTalk()
    return HttpResponse(tt.getTweets())