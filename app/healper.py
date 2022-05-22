import os, json
import requests

from languages import get_lang_ext
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

path = 'submissions'
browser = webdriver.Chrome(ChromeDriverManager().install())

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
    return new_dict

def process_data(data):
    for submission in data['result']:
        if(submission['verdict'] == 'OK' and visited.get(submission['id'], 0) == 0):
            id = submission['id']
            contestId = submission['contestId']
            code = get_code(id, contestId)
            file_name = submission['problem']['name'].replace(' ', '_') + get_lang_ext(submission['programmingLanguage'])
            save(path, file_name, code)
            visited[id] = True
            
def get_code(id, contestId):
    url = f"https://codeforces.com/contest/{contestId}/submission/{id}"
    res = requests.get(url)
    browser.get(url)
    return browser.find_element_by_id('program-source-text').text

visited = load_visited()
