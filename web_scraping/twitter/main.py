import json, csv, cmd
import district_users as du
import twitter_scraping as ts

def save_to_json(dict):
    json_dict = json.dumps(dict)
    f = open("tweet_data.json","w")
    f.write(json_dict)
    f.close()
    
def save_to_csv(list, file_name):
    headers = ["district", "term", "created_at", "text"]
    with open(file_name, "w", encoding='UTF-8') as f:
        write = csv.writer(f, lineterminator = '\n')
        write.writerow(headers)
        write.writerows(list)
    
def save_to_txt(list):
    with open("tweet_data.txt", "w", encoding='UTF-8') as f:
        f.write(str(list))


# main function which gathers and saves all tweets from district user list
def main():
    all_tweets = []
    district_users = du.get_user_list()
    # test = ['EPISD_DualLang', 'NewarkBilingual', 'LADatDCPS', 'ccsd_ell', 'sdp_multilingua']
    print(f"Gathering tweet data from: {district_users}")
    for district in district_users:
        print("---------------------------------------------------------")
        tweet_list = ts.generate_tweet_list(district)
        all_tweets += tweet_list
    total_tweets = len(all_tweets)
    total_districts = len(district_users)
    print(f"Found {total_tweets} total tweets from {total_districts} districts")
    save_to_txt(all_tweets)
    save_to_csv(all_tweets, "tweet_data.csv")

# REPL class to interact with Twitter API with utility methods
class TwitterShell(cmd.Cmd):
    """ Basic REPL for gathering data with Twitter API """
    intro = """\n Basic REPL for gathering data with Twitter API. 
    Type help or ? to list commands.\n"""
    prompt= ">>> "

    # fields used in tweet scraping
    query_params = {
        # "url": "",
        "tweet.fields": [],
        "query": None, 
        "max_results": 100,
    }
    users = []
    terms = []
    tweets = []
    fields = {
        "params": query_params,
        "users": users,
        "terms": terms,
        "tweets": tweets,
    }

    # methods to interact with fields
    def do_add_great_city(self, args):
        "Adds twitter handles from great city schools list to users"
        id, =  parse(args)
        users = du.get_user_list()
        self.users += users

    def do_gen_tweets(self, args): 
        "Generate tweet list from users, terms, and params"
        for user in self.users:
            t = ts.generate_tweet_list(user, terms=self.terms)
            self.tweets += t

    def do_add_user(self, args):
        "Add twitter handle to query: add_user [username]"
        user, = parse(args)
        self.users.append(user)
        print(f"adding {user}... \nusers: {self.users}")

    def do_add_term(self, args):
        "Add search term to query: add_term [term]" 
        term, = parse(args)
        self.terms.append(term)
        print(f"adding {term}... \nterm: {self.terms}")

    def do_edit_params(self, args):
        "Edit query params: edit [param_name] [new_param]"
        input = parse(args)
        if len(input) != 2:
            print("Number of arguments must be 2")
            return
        param_name, new_param = parse(args)
        if param_name not in self.query_params: 
            print("param_name must be one of:\n")
            print("\n".join(list(self.query_params.keys())))
            return
        self.query_params[param_name] = new_param

    # utility methods
    def do_print(self, arg):
        "Print current values: print [value] or print all"
        field, = parse(arg)
        if field == "all": 
            # print all except tweets
            for key in self.fields.keys():
                if key == "tweets" and self.tweets:
                    print(f"{key}: {len(self.tweets)} tweets; use save_tweets to save or print tweets to view")
                    continue
                print(f"{key}: {self.fields[key]}")
        elif field in self.fields.keys(): 
            print(f"{field}: {self.fields[field]}")
        else:
            print("please print one of:\n")
            print("\n".join(list(self.fields.keys())))
    
    def do_save_tweets(self, args): 
        "Save tweets to file: save_tweets [filename]"
        file, = parse(args)
        save_to_csv(self.tweets, file)
        print(f"saving {len(self.tweets)} to {file}")

    def do_quit(self, arg):
        "Quits the REPL"
        print("Quitting Twitter REPL...")
        # TODO: add teardown methods

        quit()

def parse(str): 
    return tuple(str.split(" "))

if __name__ == '__main__':
    # main()
    TwitterShell().cmdloop()