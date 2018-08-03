import sys
import json

import requests

if __name__ == "__main__":
    username = sys.argv[1]

    # Retrieve a list of "events" associated with the given user name
    response = requests.get(f"https://api.github.com/users/{username}/events")
    events = json.loads(response.content)

    # Print out the time stamp associated with the first event in that list.
    print(events[0]['created_at'])
