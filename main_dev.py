import requests
import json

url = "https://raw.githubusercontent.com/ingcoty/tank_mmonitor/master/"
headers = {"accept": "application/json"} 


def process_version_url(repo_url, filename):
    """ Convert the file's url to its assoicatied version based on Github's oid management."""

    # Necessary URL manipulations
    version_url = repo_url.replace("raw.githubusercontent.com", "github.com")  # Change the domain
    version_url = version_url.replace("/", "§", 4)                             # Temporary change for upcoming replace
    version_url = version_url.replace("/", "/latest-commit/", 1)                # Replacing for latest commit
    version_url = version_url.replace("§", "/", 4)                             # Rollback Temporary change
    version_url = version_url + filename                                       # Add the targeted filename
    return version_url


version = process_version_url(url, "main.py")
print(version)
resp = requests.get(url=version, headers=headers)

data = json.loads(resp.text)
print(data)

exit()

import time
from sr04t import Srt04t


sensor = Srt04t(triger_pin=13, echo_pin=12)

while True:
    pulse = sensor.read_distance()
    print(pulse)
    time.sleep(5)

