# Write a Python program that write data in csv file using pandas of ISS Location with timestamp min 100 records 
#Use this url to get the data of ISS (Url: http://api.open-notify.org/iss-now.json) 

import requests
import pandas as pd
import time

# Define the API endpoint URL
url = "http://api.open-notify.org/iss-now.json"

# Initialize an empty list to store the data
data = []

# Number of records to collect
num_records = 10


# Collect data
for _ in range(num_records):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            iss_data = response.json()

            # Extract latitude, longitude, and timestamp
            latitude = iss_data['iss_position']['latitude']
            longitude = iss_data['iss_position']['longitude']
            timestamp = iss_data['timestamp']

            # Append the data to the list
            data.append({"Timestamp": timestamp, "Latitude": latitude, "Longitude": longitude})

            # Print progress
            print(f"Record {_+1}/{num_records} collected.")
        
        else:
            print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        # Catch any request exceptions and print the error
        print(f"An error occurred: {e}")

    # Wait for a short interval before the next request to avoid being blocked by the server
    time.sleep(1)

# Convert the list of data into a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv("iss_location_data.csv", index=False)

print("Data collection complete. CSV file 'iss_location_data.csv' created.")
