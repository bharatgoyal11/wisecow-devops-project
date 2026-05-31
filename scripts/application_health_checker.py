import requests

URL = "https://www.google.com"

try:
    response = requests.get(URL)

    if response.status_code == 200:
        print(f"{URL} is UP")
    else:
        print(f"{URL} is DOWN")
        print(f"Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error checking application: {e}")