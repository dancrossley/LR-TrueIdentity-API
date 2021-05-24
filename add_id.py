import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) # Ignore certificate errors

###########################
# Change these 
pm = 'UKRD1SEXM-01' # URL / IP of the PM
filename = "C:\\Users\dcrossley\\Documents\\test.txt" # Put the fullpath to the file with the usernames here, double escape the folders, ie '\\'
email_suffix = '@logrhythm.com' # This is used for the unique identifier for the Identity
api_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE1LCJqdGkiOiI3NTY3ZGUwMi1iNWEzLTQ4NzItYjVlMi1lZDAyNjg4Y2U3OTUiLCJjaWQiOiI1RkEyOUEyNi1FREJBLTQ4RjQtQTM5RC02M0I3RTFDQ0I1NjkiLCJpc3MiOiJsci1hdXRoIiwicmlkIjoiZ2xvYmFsQWRtaW4iLCJwaWQiOjE1LCJzdWIiOiJVS0NYQ1xcZGNyb3NzbGV5IiwiZXhwIjoxNjUzMzY0NjE2LCJkZWlkIjoxLCJpYXQiOjE2MjE4Mjg2MTZ9.JcjoC_ZBuUN7qB5QDdblDAtM6Zn56jbhWcScMJkqO4IqJgCBN_QclzxtZyBMuKPzib-gz9dcyImxDytIPXml5GijNCigEnl19KTbDaEgxvDD3nsf2CIYj0zAeJ_h48pCAJjzUJj4zTzoOL9HGfnOMVyZZ5hB7WatzJu16pmFCgZETduHCmbQHG3CTNBHAgIKXetxyf4Cfp9-DRUD-TBexQdXeGkHrjzUMmKTXdshmzT-ooxn-_WhEGcRyjzWYLHeVZXnBQlKL_RSgPapJtvHXQGAKQ6KcBCRFxnyAEtzH7lYkhl5CFVcKxOWXAOhzM0CJIykAmm381TesorWRwwCNQ'
###########################

url = ("https://%s:8501/lr-admin-api/identities/bulk/?entityID=1" % pm)

def process_names(filename):
    # reads firstname.lastname from a textfile and posts it to the API as an Identity
    f = open(filename)
    l = f.readlines()
    for n in l: # Read through each line in file
        try:
            m = n.index('.') # Split firstname from lastname
        except:
            continue
        nameFirst = n[:m].capitalize() 
        nameLast = n[m+1:].rstrip().capitalize()
        login = n.rstrip()
        identity = '{"friendlyName":"' + nameFirst + ' ' + nameLast + '","accounts":[{"nameFirst":"' + nameFirst + '","nameLast":"' + nameLast + '", "vendorUniqueKey": "' + nameFirst + '.' + nameLast + email_suffix + '","identifiers":[{"identifierType":"Login","value":"' + login + '"}]}]}\n'
        call_api(identity)
    
def call_api(identity):
    # Posts identity to the LogRhythm AP
    t = 'Bearer ' + api_token
    headers = {
    'Authorization': t,
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = identity, verify=False)
    print(response.text.encode('utf8'))

process_names(filename)