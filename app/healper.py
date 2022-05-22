import os, json, time

from languages import get_lang_ext
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

path = 'submissions'
options = Options()
options.headless = True
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

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
        id = submission['id']
        contestId = submission['contestId']
        file_name = submission['problem']['name'].replace(' ', '_') + get_lang_ext(submission['programmingLanguage'])
        if(submission['verdict'] == 'OK' and visited.get(file_name, -1) < id):
            code = get_code(id, contestId)
            save(path, file_name, code)
            visited[file_name] = id
            
def get_code(id, contestId):
    url = f"https://codeforces.com/contest/{contestId}/submission/{id}"
    browser.get(url)
    time.sleep(0.2)
    try:
        return browser.find_element_by_id('program-source-text').text
    except:
        raise Exception(f"too many requests, try again later, last submisson id: {id}, contestId: {contestId}")

visited = load_visited()
