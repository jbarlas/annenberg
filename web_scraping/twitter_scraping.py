import requests
import json 
import auth
import time

search_terms = ["tutor", "tutoring", "tutors"]

def create_url(term, district):
    base_url = 'https://api.twitter.com/2/tweets/search/all'
    query = f"query={term}%20from:{district}"
    start_time = "start_time=2010-01-01T00:00:00.000Z" # from 2010 onwards
    url = f"{base_url}?{query}&{start_time}"
    return url


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=auth.bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json().get('data')

def get_list_tweets(json):
    list_tweets = []
    if json is None:
        return list_tweets
    for tweet in json:
        list_tweets.append(tweet.get("text"))
    return list_tweets


def generate_tweet_list(district):
    tweet_list = []
    for term in search_terms:
        print(f'Getting tweets from {district} with term: {term}...')
        url = create_url(term, district)
        json_resp = connect_to_endpoint(url)
        tweets = get_list_tweets(json_resp)
        num_tweets = len(tweets)
        print(f"{num_tweets} tweets found")
        tweet_list.append(tweets)
        time.sleep(1)
    return tweet_list


def main():
    tl = generate_tweet_list("nycschools")
    print(tl)

if __name__ == '__main__':
    main()

        


