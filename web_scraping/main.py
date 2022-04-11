import json
import csv
import district_users as du
import twitter_scraping as ts

def save_to_json(dict):
    json_dict = json.dumps(dict)
    f = open("tweet_data.json","w")
    f.write(json_dict)
    f.close()
    
def save_to_csv(list):
    headers = ["district", "term", "created_at", "text"]
    with open("tweet_data.csv", "w", encoding='UTF-8') as f:
        write = csv.writer(f, lineterminator = '\n')
        write.writerow(headers)
        write.writerows(list)
    
def save_to_txt(list):
    with open("tweet_data.txt", "w", encoding='UTF-8') as f:
        f.write(str(list))


def main():
    all_tweets = []
    district_users = du.get_user_list()
    test = ['EPISD_DualLang', 'NewarkBilingual', 'LADatDCPS', 'ccsd_ell', 'sdp_multilingua']
    print(f"Gathering tweet data from: {district_users}")
    for district in district_users:
        print("---------------------------------------------------------")
        tweet_list = ts.generate_tweet_list(district)
        all_tweets += tweet_list
    total_tweets = len(all_tweets)
    total_districts = len(district_users)
    print(f"Found {total_tweets} total tweets from {total_districts} districts")
    save_to_txt(all_tweets)
    save_to_csv(all_tweets)


if __name__ == '__main__':
    main()