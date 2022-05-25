import auth
import requests
import time

BASE_URL = "https://api.twitter.com/2/tweets/counts/all"

def create_url(district, next_token=""):
    query = f"from:{district}&start_time=2010-01-01T00:00:00.000Z&granularity=day"
    if next_token:
        query += f"&next_token={next_token}"
    url = f"{BASE_URL}?query={query}"
    # print(url)
    return url

def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=auth.bearer_oauth,)
    # print(response.status_code)
    if response.status_code == 429:
        time.sleep(60)
        connect_to_endpoint(url)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    meta = response.json().get("meta")
    return meta.get("total_tweet_count"), meta.get("next_token"), response.json().get("data")[-1].get("end")

def main():
    district = "JPSDistrict"
    total_tweet = 0
    next_val = True
    next_token = ""
    while next_val:
        count, token, endDate = connect_to_endpoint(create_url(district, next_token))
        print(f"tweets collected until {endDate[:11]}: {count}")
        total_tweet += count
        if token:
            next_token = token
        else:
            next_val = False
    print("----------------------------------------------")
    print(f"Total Tweets for {district} since 2010: {total_tweet}")

if __name__ == "__main__":
    main()