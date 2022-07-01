# Twitter Scraping

## Authorization Setup:

1. Create a folder within `web_scraping` entittled `secret`
2. Create a file within this folder entitled `auth_token.py`
3. Copy and paste the following code into the file:
```
AUTH_TOKEN = "<auth_token>"
```
4. Replace auth_token with the organization Twitter API authentication token (ensure it is declared as a string)
## How to run:

1. Setup
   - Ensure that you have Python 3.x installed and set as active interpreter
   - Ensure that you have followed the authorization steps
2. Run `main.py` 
   - This can be done in the parent directory by running the following command:
   - `python web_scraping/twitter/main.py`
3. This will open a REPL with commands to interact with the Twitter API
4. Type `help` to view all commands or type `help [command]` to view command usage