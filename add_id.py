import requests
import json

url = "https://UKRD1SEXM-01:8501/lr-admin-api/identities/bulk/?entityID=1"

payload = {"friendlyName":"Boris Johnson3","accounts":[{"nameFirst":"Boris","nameLast":"Johnson","identifiers":[{"identifierType":"Login","value":"bojo"}]}]}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE1LCJqdGkiOiI3NTY3ZGUwMi1iNWEzLTQ4NzItYjVlMi1lZDAyNjg4Y2U3OTUiLCJjaWQiOiI1RkEyOUEyNi1FREJBLTQ4RjQtQTM5RC02M0I3RTFDQ0I1NjkiLCJpc3MiOiJsci1hdXRoIiwicmlkIjoiZ2xvYmFsQWRtaW4iLCJwaWQiOjE1LCJzdWIiOiJVS0NYQ1xcZGNyb3NzbGV5IiwiZXhwIjoxNjUzMzY0NjE2LCJkZWlkIjoxLCJpYXQiOjE2MjE4Mjg2MTZ9.JcjoC_ZBuUN7qB5QDdblDAtM6Zn56jbhWcScMJkqO4IqJgCBN_QclzxtZyBMuKPzib-gz9dcyImxDytIPXml5GijNCigEnl19KTbDaEgxvDD3nsf2CIYj0zAeJ_h48pCAJjzUJj4zTzoOL9HGfnOMVyZZ5hB7WatzJu16pmFCgZETduHCmbQHG3CTNBHAgIKXetxyf4Cfp9-DRUD-TBexQdXeGkHrjzUMmKTXdshmzT-ooxn-_WhEGcRyjzWYLHeVZXnBQlKL_RSgPapJtvHXQGAKQ6KcBCRFxnyAEtzH7lYkhl5CFVcKxOWXAOhzM0CJIykAmm381TesorWRwwCNQ',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload), verify=False)

print(response.text.encode('utf8'))
