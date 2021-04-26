import requests

url = "https://192.168.0.21/command-api"
auth = {'username':'arista','password':'aristadzjy'}


commands = open("eth2.json", "r")

r = requests.post(url, auth=('arista','aristadzjy'), data=commands, verify=False) 

print(r.text)