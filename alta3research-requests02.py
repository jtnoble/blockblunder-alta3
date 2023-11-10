import requests
from pprint import pprint

def main():
    api_url = "http://127.0.0.1:5000/api/inventory/json"
    query = "?query=Shrek"  # Adding a query to make the output not be 600k lines
    api_url += query
    print(api_url)
    response = requests.get(api_url)
    pprint(response.json())

if __name__ == '__main__':
    main()