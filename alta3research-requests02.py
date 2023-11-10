import requests
from pprint import pprint

def get_req():
    api_url = "http://127.0.0.1:2224/api/inventory/json"
    query = "?query=Shrek"  # Adding a query to make the output not be 600k lines
    api_url += query
    response = requests.get(api_url)
    pprint(response.json())

def post_req():
    api_url = "http://127.0.0.1:2224/api/inventory/checkout"
    data = {"id": 30593}    # This is Shrek 1
    response = requests.post(url=api_url, json=data)
    pprint(response.text)

def main(post):
    get_req()
    if post:
        post_req()

if __name__ == '__main__':
    main(True)