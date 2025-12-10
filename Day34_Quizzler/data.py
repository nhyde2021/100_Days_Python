import requests
import urllib3

urllib3.disable_warnings()

parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get(url="http://opentdb.com/api.php", params=parameters, verify=False)
data.raise_for_status()
question_data = data.json()["results"]



