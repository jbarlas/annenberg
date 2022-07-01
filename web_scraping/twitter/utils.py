"""Utiity funcions for Twitter web scraping"""

from enum import Enum
import requests
import time
import auth
import csv

"""
URL Helpers:
functions which generate routes to hit 
based on query parameters
"""

from typing import List, Optional

class TweetFields(Enum):
    CREATED_AT = "created_at"



# TODO: create function which generates api url to hit based on parameters
def url_all_tweets(search_term=None, account_name=None, fields=Optional[List[TweetFields]]):
    base_url_all_tweets = 'https://api.twitter.com/2/tweets/search/all'
    query = []
    if search_term: 
        query.append(f"query={search_term}")
    if account_name: 
        query.append(f"from:{account_name}")
    query = f"query={search_term}%20from:{account_name}"
    if fields: 
        # tweet_fields = f"tweet.fields={fields.join(",")}"
        pass
    fields = f"tweet.fields=created_at,text"
    start_time = "start_time=2010-01-01T00:00:00.000Z" # from 2010 onwards
    url = f"{base_url_all_tweets}?{query}&{start_time}&{fields}"
    return url


def connect_to_endpoint(url, timeout=60):
    response = requests.request("GET", url, auth=auth.bearer_oauth,)
    if response.status_code == 429: # too many requests
        # timeout and try again
        time.sleep(timeout)
        connect_to_endpoint(url)
    
    if response.status_code != 200: # bad request
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}"
        )
    return response.json().get('data')

def save_to_csv(list, headers=None):
    with open("tweet_data.csv", "w", encoding='UTF-8') as f:
        write = csv.writer(f, lineterminator = '\n')
        if headers:
            write.writerow(headers)
        write.writerows(list)
    
def save_to_txt(list):
    with open("tweet_data.txt", "w", encoding='UTF-8') as f:
        f.write(str(list))