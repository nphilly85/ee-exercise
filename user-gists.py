import urllib.request
import json
import yaml
import argparse

class UserGists:
    def __init__(self, github_username, latest_gist_yaml_file="{}-latest_gist.yaml"):
        self.github_username = github_username
        self.latest_gist_yaml_file = latest_gist_yaml_file.format(github_username)
        self.gists_url = "https://api.github.com/users/{}/gists?since={}"
        
    def get_gists(self):
        self.gists = {}
        latest_gist_datetime = ""
        
        try:
            with open(self.latest_gist_yaml_file, "r") as file:
                latest_gist = yaml.safe_load(file)
                
            if latest_gist['latest-gist']:
                latest_gist_datetime = latest_gist['latest-gist']
                print("Fetching all public gists for user: {}".format(self.github_username))

        except FileNotFoundError:
            print("First run, fetching all gists")

        response = urllib.request.urlopen(self.get_gists_url(latest_gist_datetime))
        json_content = response.read()
        self.gists = json.loads(json_content)
        return self.gists
        
    def get_gists_url(self, latest_gist_datetime=""):
        return self.gists_url.format(self.github_username,latest_gist_datetime)
        
    def store_latest_gist_datetime(self, latest_gist_datetime):
        try:
            latest_gist = {
                'latest-gist': latest_gist_datetime
            } 
            with open(self.latest_gist_yaml_file, "w") as file:
                yaml.dump(latest_gist, file)
        except Exception as e:
            print("Failed to store latest gist timestamp because: {}".format(e))
            
    def list_gists(self):
        gists = self.get_gists()
        if len(gists) == 0:
            print("No gists found")
        else:
            latest_gist_datetime = gists[0]['created_at']
            self.store_latest_gist_datetime(latest_gist_datetime)
            
            print("Listing public gists for github user:{}".format(self.github_username))
            print("Latest gist timestamp: {}" .format(latest_gist_datetime))

            print('=' * 50)
            for _gist in gists:
                print("Gist URL: {}".format(_gist['html_url']))
                print("Gist API URL: {}".format(_gist['url']))
                print("Gist Description: {}".format(_gist['description']))
                print("Gist ID: {}".format(_gist['id']))
                print("Gist Creation DateTime: {}".format(_gist['created_at']))
                print('=' * 50)
                

parser = argparse.ArgumentParser(description="User gist checker")
parser.add_argument("--username", required=True, help="The github username in which to pull public gists from")
args = parser.parse_args()

gist_checker = UserGists(args.username)
gist_checker.list_gists()
