#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth

authURL = "https://192.168.0.5/web/api/#!/login/authenticate_do"
url = "https://192.168.0.5/cvpservice/configlet/getConfigletByName.do?name="
infra_configlet = "ATD-INFRA"


login_data = {
  "password": "arista9wtf",
  "userId": "arista"
}

username = "arista"
password = "arista9wtf"


response = requests.get(url+infra_configlet, verify=False, auth=(username, password))

print(response.status_code)

