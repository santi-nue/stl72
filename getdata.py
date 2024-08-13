import requests
import time
import json

# Define the API endpoint
api_url = "https://api.adsb.one/v2/point/39.912781/32.788112/60" 
# Define the number of requests and the delay
num_requests = 100
delay = 4  # seconds

# Open a file to write the JSON responses
with open('responses.json', 'w') as outfile:
    # Initialize a list to hold the responses
    responses = []
    
    for i in range(num_requests):
        try:
            # Make the HTTPS request
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Append the JSON response to the list
            responses.append(response.json())
            print(f"Request {i + 1}: Success")
        
        except requests.exceptions.RequestException as e:
            print(f"Request {i + 1}: Failed - {e}")
        
        # Wait for the specified delay before the next request
        time.sleep(delay)
    
    # Write all responses to the file in JSON format
    json.dump(responses, outfile, indent=4)
    print("All responses have been written to responses.json")
