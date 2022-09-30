import json
import requests
import pprint

def dowellconnection(cluster,database,collection,document,team_member_ID,function_ID,command,field):
    url = "http://100002.pythonanywhere.com/"
        #searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
    payload = json.dumps({
        "cluster": cluster,
        "database": database,
        "collection": collection,
        "document": document,
        "team_member_ID": team_member_ID,
        "function_ID": function_ID,
        "command": command,
        "field": field,
        "update_field": {
            "order_nos": 21
            },
        "platform": "bangalore"
        })
    headers = {
        'Content-Type': 'application/json'
        }

    response = requests.request("POST", url, headers=headers, data=payload)
    res= json.loads(response.text)

    return res