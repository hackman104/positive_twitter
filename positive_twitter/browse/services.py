import os
from pprint import pprint

import twitter

api = twitter.Api(consumer_key=os.environ.get('PT_CONS_API_KEY'),
                  consumer_secret=os.environ.get('PT_CONS_SECRET_KEY'),
                  access_token_key=os.environ.get('PT_ACCESS_TOKEN'),
                  access_token_secret=os.environ.get('PT_ACCESS_TOKEN_SECRET'))


def get_recent():
    results = api.GetSearch(
        raw_query="q=pittsburgh&result_type=recent&count=10")
    good_results = [
        result for result in results if not result.possibly_sensitive]
    pprint(good_results)
    return good_results
