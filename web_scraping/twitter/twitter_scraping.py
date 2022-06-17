import requests
import json 
import auth
import time

search_terms = ["tutor", "tutoring", "tutors"]

def create_url(term, district):
    base_url = 'https://api.twitter.com/2/tweets/search/all'
    query = f"query={term}%20from:{district}"
    fields = f"tweet.fields=created_at,text"
    start_time = "start_time=2010-01-01T00:00:00.000Z" # from 2010 onwards
    url = f"{base_url}?{query}&{start_time}&{fields}"
    return url


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=auth.bearer_oauth,)
    print(response.status_code)
    if response.status_code == 429:
        time.sleep(60)
        connect_to_endpoint(url)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json().get('data')

def get_list_tweets(district, term, json_resp):
    list_all_tweet = []
    print(json_resp)
    if json_resp is None:
        return [[district, term, "", ""]]
    for tweet in json_resp:
        tweet_list = []
        tweet_list.append(district)
        tweet_list.append(term)
        tweet_list.append(tweet.get("created_at"))
        tweet_list.append(tweet.get("text"))
        clean_tweet = list(map(lambda t: t.replace(",", "").replace('\n', ""), tweet_list))
        list_all_tweet.append(clean_tweet)
    return list_all_tweet


def generate_tweet_list(district):
    tweet_list = []
    for term in search_terms:
        print(f'Getting tweets from {district} with term: {term}...')
        url = create_url(term, district)
        json_resp = connect_to_endpoint(url)
        tweets = get_list_tweets(district, term, json_resp)
        num_tweets = len(tweets)
        print(f"{num_tweets} tweets found")
        tweet_list += tweets
        time.sleep(3)
    return tweet_list


def main():
    print(generate_tweet_list("ebrpschools"))
    print(generate_tweet_list("EPISD_DualLang"))

if __name__ == '__main__':
    main()

        


