import requests
import auth

GREAT_SCHOOLS_ID = 54752906


def create_url(id=str(GREAT_SCHOOLS_ID)):
    "Creates url for user list search from given list id"
    base_url = "https://api.twitter.com/2/lists/" + id + "/members?"
    query = "user.fields=username"
    # maybe try to also get max values
    url = base_url + query
    return url


def connect_to_endpoint(url):
    "Sends get request to given url with auth"
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
    "Gets just the username from returned twitter data json object"
    user_list = []
    districts = json.get("data")
    for district in districts:
        user_list.append(district.get("username"))
    return user_list

def get_user_list(): 
    "Generates list of users"
    url = create_url()
    json_resp = connect_to_endpoint(url)
    user_list = strip_username(json_resp)
    return user_list


def main():
    url = create_url()
    json_resp = connect_to_endpoint(url)
    user_list = strip_username(json_resp)
    print(f"{len(user_list)} districts: {user_list}")

if __name__ == '__main__':
    main()
