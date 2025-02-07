import requests
from time import sleep
from tqdm import tqdm

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'connection': 'keep-alive'
}

urls_list = []
with open('input.txt', 'r') as file:
    dois = file.readlines()

for doi in tqdm(dois):
    try:
        response = requests.get(f'https://www.doi.org/{doi.strip()}', headers=headers, timeout=10)
        journals = response.url
        urls_list.append(journals)
        sleep(2)  # Adding a short sleep to be polite to the server
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving DOI {doi.strip()}: {e}")
        urls_list.append(f"Error retrieving DOI {doi.strip()}")

with open('journal_url_list.csv', 'w') as file:
    file.write('doi,url\n')  # Adding column headers
    for doi, url in zip(dois, urls_list):
        file.write(f'{doi.strip()}, {url}\n')
