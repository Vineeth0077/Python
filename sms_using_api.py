


import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
	"authorization": "Hp0zfOrEImTd4sVP6KuX5oaSkDqMCwW92hFivctjnAxbNleYZR7f31yiZtXhELHOncSqprwBJRFIjd64",
	"message": "This is test Message sent from Python Script using REST API.",
	"language": "english",
	"route": "q",
	"numbers": "7337504290"}

headers = {
	'cache-control': "no-cache"
}
try:
	response = requests.request("GET", url,
								headers = headers,
								params = querystring)
	
	print("SMS Successfully Sent")
except:
	print("Oops! Something wrong")
