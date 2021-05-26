import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) # Ignore certificate errors

###########################
# Change these 
pm = '127.0.0.1:8501' # URL / IP of the PM along with the port if its on-prem. For example 'x.x.x.x:8501'. Omit the ':8501' for LR Cloud.
filename = "C:\\Users\dcrossley\\Documents\\test.txt" # Put the fullpath to the file with the usernames here, double escape the folders, ie '\\'
email_suffix = '@logrhythm.com' # This is used for the unique identifier for the Identity
api_token = ''
###########################

url = ("https://%s/lr-admin-api/identities/bulk/?entityID=1" % pm)

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
    # Posts identity to the LogRhythm API
    t = 'Bearer ' + api_token
    headers = {
    'Authorization': t,
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = identity, verify=False)
    print(response.text.encode('utf8'))

process_names(filename)