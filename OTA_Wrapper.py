from OTA_Updater import OTA_Updater
from wifi_config import SSID, PASSWORD
import urequests
import json


class OTA_Wrapper:

    def __init__(self, github_url: str):
        self.github_url = github_url
        self.headers = {"accept": "application/json"} 
        try:
            resp = urequests.get(self.github_url, headers=self.headers)
            if resp.status_code == 200:
                data = json.loads(resp.text)
                files = [file["name"] for file in data["payload"]["tree"]["items"]]
                for file in files:
                    OTA_Updater(ssid=SSID, password=PASSWORD, repo_url=self.github_url, filename=file)
        except:
            print("!Error getting github files...")


