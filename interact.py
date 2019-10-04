import requests
import json

config_file = open("config.json", 'a+')

try:
    data = json.load(config_file)
except:
    AUTH_TOKEN = raw_input("Please enter a valid AUTH_TOKEN to be used : ")
    data = {'AUTH_TOKEN':"%s" % (AUTH_TOKEN)}
    json.dump(data,config_file)

s = requests.Session()
s.headers.update({
    "Authorization": "Bearer %s" % (data['AUTH_TOKEN']),
    "Content-Type": "application/json"
})

def request_api (url, file_prefix):
    response = s.get(url)
    with open("%s.json" % (file_prefix), 'w') as outf:
        outf.write(response.content)

# Survey IDs
surveys = ["270422199", "270422293", "270421449"]

for x in surveys:
    url = "https://api.surveymonkey.com/v3/surveys/%s/responses/bulk" % (x)
    request_api(url, "responses_bulk")