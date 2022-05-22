import requests, os
from time import sleep
from healper import process_data, dumb_visited_problems
URL = "https://codeforces.com/api/user.status"
FROM = 1
COUNT = 200

def app():
    with requests.Session() as s:
        params = {
            'handle' : os.environ['CF_USER'],
            'from' : FROM,
            'count' : COUNT
        }
        res = s.get(URL, params=params)
        print('...Processing...')
        try:
            while(res.ok):
                data = res.json()
                process_data(data)
                if(data['result']):
                    params['from'] += COUNT
                    sleep(2.5)
                    res = requests.get(URL, params=params)
                else:
                    print('...Done...')
                    return
            print('Request Problem...\nstatus_code: ' + res.status_code)
        except Exception as e:
            print(e)
        finally:
            dumb_visited_problems()
if __name__ == '__main__':
    app()
