from django.http import HttpResponse
from django.shortcuts import render
import twitter

api = twitter.Api(consumer_key=[consumer key],
                  consumer_secret=[consumer secret],
                  access_token_key=[access token],
                  access_token_secret=[access token secret])


def index(request):
    return HttpResponse("This is a placeholder for the main page.")
