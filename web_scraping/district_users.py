import requests
import json
import auth

def create_url():
    base_url = "https://api.twitter.com/1.1/users/search.json?"
    query = "q=school%20district"
    # maybe try to also get max values
    url = base_url + query
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
    return response.json()

def strip_username(json): 
    user_list = []
    for district in json:
        user_list.append(district.get("screen_name"))
    return user_list

def get_user_list(): 
    url = create_url()
    json_resp = connect_to_endpoint(url)
    user_list = strip_username(json_resp)
    return user_list
    

def main():
    url = create_url()
    json_resp = connect_to_endpoint(url)
    user_list = strip_username(json_resp)
    print(user_list)

if __name__ == '__main__':
    main()
