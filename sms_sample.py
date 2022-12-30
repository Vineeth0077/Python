


import requests

url = "https://www.fast2sms.com/dev/bulkV2"

message = 'Hey hi .. this is your friend'

numbers="7337504290"

payload = f'sender_id = FTWSMS&message={message}&route=v3&language=english&numbers={numbers}'

headers = {
	"authorization": "Hp0zfOrEImTd4sVP6KuX5oaSkDqMCwW92hFivctjnAxbNleYZR7f31yiZtXhELHOncSqprwBJRFIjd64",
	'CONTENT-TYPE':'application/x-www-form-urlencoded'
    }

response = requests.request("POST",url=url,data = payload,headers=headers)

print(response.text)