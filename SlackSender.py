import requests
import json
import datetime
import os

DataFolder = './Cache'
DataFile = 'Data.txt'

token = None

def post_message(channel, text):
    global token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token
    }
    payload = {
        'channel': channel,
        'text': text
    }
    r = requests.post('https://slack.com/api/chat.postMessage',
        headers = headers,
        data = json.dumps(payload)
        )
    if r.status_code == 200:
        print("SEND [ OK ] - %s"%(datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')))

if __name__ == "__main__":
    try:
        f = open(DataFolder+"/"+DataFile, "r", encoding='utf-8')
        Data = f.read()
    except:
        exit(0)

    if len(Data) <= 0:
        exit(0)
    if os.path.isfile(DataFolder+"/"+DataFile):
        pass
    else:
        exit(0)

    
    post_message("#logbot", Data)
    os.remove(DataFolder+"/"+DataFile)