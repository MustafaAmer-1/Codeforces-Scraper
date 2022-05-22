# Codeforces-Scraper
## Description
This script helps you to scrape all your solutions in [Codeforces](https://codeforces.com/) to a directory in your local machine.

This script is inspired by [Leetcode-scraper](https://github.com/mosta7il/Leetcode-scraper)

## Requirements
You must have `Python3` installed alongside with `pip3`

## Run
if you can run bash scripts you can use [scrap.sh](/scrap.sh)
first edit the [scrap.sh](/scrap.sh) with your Codeforces Handle then run
```bash
bash ./scrap.sh
```
or you can do it the manual way
1. create an empty directory named `submissions`
2. make an enviroment variable named `CF_USER` with its value equal to your Codeforces Handle. (Google how to make this variable in your OS)
2. install the required packages by `pip3 install -r requirements.txt`
3. run the script by `python3 app/application.py`

after the script finishes it's execution the source files will be located in submissions folder.

## Features

- The script saves the history of the already visited problems so if you run it again only the un scraped problems will be affcted unless you add another new submission to an old scrapped problem.
- The script saves the most racent submission for the same problem.
