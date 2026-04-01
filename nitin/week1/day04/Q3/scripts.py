import requests
import time

url =  "https://api.github.com/users/torvalds"

def fetch_with_retry(url, max_retires = 3):
    for attempt in range(1,max_retires+1):
        response = requests.get(url)
        if response.status_code == 200:
            print("Attempt", attempt)
            break
        elif response.status_code == 429:
            wait = int(response.headers.get("Retry-After", 60)) 
            print(f"Wait for {wait} seconds")
            time.sleep(wait)
    else:
        print("All retries failed")

fetch_with_retry(url)
