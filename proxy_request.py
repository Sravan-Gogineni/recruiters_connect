import requests

# Make a request through the proxy
url = "http://www.google.com"
response = requests.get(url)

# Print the response
print(response.status_code)
print(response.json())