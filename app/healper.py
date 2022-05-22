import os, json, requests

from languages import get_lang_ext
from bs4 import BeautifulSoup

path = 'submissions'
session = requests.Session()

def save(path, filename, content):
    with open(os.path.join(path, filename), 'w+') as file:
        file.write(content)

def dumb_visited_problems():
    with open('history.json', 'w+') as file:
        json.dump(visited, file)

def load_visited():
    try:
        with open('history.json', 'r+') as file:
            new_dict = json.load(file)
    except ValueError:
        new_dict = {} 
    new_dict['invalid_submission'] = []
    return new_dict

def process_data(data):
    for submission in data['result']:
        id = submission['id']
        contestId = submission['contestId']
        file_name = submission['problem']['name'].replace(' ', '_') + get_lang_ext(submission['programmingLanguage'])
        if(submission['verdict'] == 'OK' and visited.get(file_name, -1) < id):
            code = get_code(id, contestId)
            if(len(code)):
                save(path, file_name, code)
                visited[file_name] = id
            else:
                visited['invalid_submission'].append({'id': id, 'contestId': contestId})
            
def get_code(id, contestId):
    url = f"https://codeforces.com/contest/{contestId}/submission/{id}"
    res = session.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    if("Illegal contest ID" in res.text):
        return ''
    if("Too many requests" in res.text):
        raise Exception(f"Too many requests, try again later, last submisson id: {id}, contestId: {contestId}")
    return soup.find(id="program-source-text").text

visited = load_visited()
