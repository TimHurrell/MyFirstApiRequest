import requests
import json
#response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
#for data in response.json()['items']:
#  if data['answer_count'] == 0:
#    print (data['title'])
response = requests.get('http://localhost:5000/myendpoint/')
print (response.json())


