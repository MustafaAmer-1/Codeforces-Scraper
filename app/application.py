import requests
from time import sleep
from healper import process_data, dumb_visited_problems
URL = "https://codeforces.com/api/user.status"
HANDLE = "MustafaAmer-1"
FROM = 1
COUNT = 20

def app():
    params = {
        'handle' : HANDLE,
        'from' : FROM,
        'count' : COUNT
    }
    res = requests.get(URL, params=params)
    print('...Processing...')
    while(res.ok):
        data = res.json()
        process_data(data)
        dumb_visited_problems()
        if(data['result']):
            params['from'] += COUNT
            sleep(2.5)
            res = requests.get(URL, params=params)
        else:
            print('...Done...')
            return
    print('Request Problem...\nstatus_code: ' + res.status_code)

if __name__ == '__main__':
    app()
