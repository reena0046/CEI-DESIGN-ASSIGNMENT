#Q5. Write a Python program using the requests module to send a GET request to a Given Below Url API endpoint and print the 
#a) latitude 
#b) longitude 
#c) timestamp 
#(Url: http://api.open-notify.org/iss-now.json) 

import requests
url = "http://api.open-notify.org/iss-now.json"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        timestamp = data['timestamp']
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Timestamp:", timestamp)
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

