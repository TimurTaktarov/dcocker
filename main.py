import sys
import datetime
import time
import requests

station = sys.argv[1:]

base_url = "http://api.open-notify.org/iss-now.json"

while True:
    response = requests.get(url=base_url)
    data = response.json()
    result = f'{datetime.datetime.now()};{data["iss_position"]} >>> {data["message"]}; timestamp: {data["timestamp"]}\n'
    print(result, end='')

    with open(f'statistic/{station}.csv', 'a') as file:
        file.write(result)
        time.sleep(5)
