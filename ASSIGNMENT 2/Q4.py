#Q4. Write a Python program using the requests module to send a GET request to a Given Below Url API endpoint and print the JSON response 
#(Url: http://api.open-notify.org/iss-now.json)
 
import requests
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("JSON Response:")
    print(data)
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
