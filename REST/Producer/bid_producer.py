import requests
import time
import random

def generate_bid():
    return random.uniform(10, 100)

def send_bid(bid):
    services = [
        'http://bid_capture:5000/bid',
        'http://bid_tracking:5001/bid',
        'http://bid_analytics:5002/bid'
    ]
    
    for service in services:
        try:
            response = requests.post(service, json={'bid': bid})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to send bid to {service}: {e}")

def main():
    while True:
        bid = generate_bid()
        print(f"Generated bid: {bid}")
        send_bid(bid)
        time.sleep(5)

if __name__ == '__main__':
    main()
