import requests
import json

def msg91(mbl,msg):


    url = "https://api.msg91.com/api/v2/sendsms"

    querystring = {"country":"91"}
    m_no = [mbl,]

    payload = {
    "sender": "ELIXIR",
    "route": "4",
    "country": "91",
    "sms": [
        {
        "message": msg,
        "to":m_no
        }
    ]
    }

    data = json.dumps(payload)

    headers = {
        'Content-Type': "application/json",
        'authkey': "269252AvOe9oq2bXtu5c99c09b",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "api.msg91.com",

        }



    response = requests.request("POST", url, data=data, headers=headers, params=querystring)

    return response.text

