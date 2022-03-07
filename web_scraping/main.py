import json
import district_users as du
import twitter_scraping as ts

def save_to_file(dict):
    json_dict = json.dumps(dict)
    f = open("tweet_data.json","w")
    f.write(json_dict)
    f.close()


def main():
    tweet_dict = {}
    district_users = du.get_user_list()
    print(f"Gathering tweet data from: {district_users}")
    for district in district_users:
        print("---------------------------------------------------------")
        tweet_list = ts.generate_tweet_list(district)
        tweet_dict[district] = tweet_list
    total_tweets = len(sum(tweet_dict.values(), []))
    total_districts = len(tweet_dict.keys())
    print(f"Found {total_tweets} total tweets from {total_districts} districts")
    save_to_file(tweet_dict)


if __name__ == '__main__':
    main()