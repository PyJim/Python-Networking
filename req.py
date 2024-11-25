import requests

# make a GET request to the URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# check if the request was successful
if response.status_code == 200:
    # print the response data
    print(response.json())
else:
    # print an error message
    print(f"Request failed with status code {response.status_code}")