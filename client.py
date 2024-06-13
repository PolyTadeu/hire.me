import requests
from routes import v1
import os
from dotenv import load_dotenv


load_dotenv()

PORT = os.getenv('PORT', '8080')
HOST = os.getenv('HOST', '0.0.0.0')

base_url = f'http://{HOST}:{PORT}/api/v1'

def shorten_url(original_url):
    endpoint = '/shorten_url'
    url = f'{base_url}{endpoint}/?url={original_url}'
    response = requests.post(url)
    return response.json()

def retrive_url(alias):
    endpoint = f'/retrive_url/{alias}'
    url = f'{base_url}{endpoint}'
    response = requests.get(url)
    return response.url

def get_most_accessed_urls():
    endpoint = '/most_accessed'
    url = f'{base_url}{endpoint}'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    # Encurtamento de URL
    original_url = 'https://example.com'
    shortened_url = shorten_url(original_url)
    print(f'URL encurtada: {shortened_url["short_url"]}')

    # Redirecionamento para URL original
    alias = shortened_url["short_url"].split('/')[-1]
    original_url = retrive_url(alias)
    print(f'Redirecionando para URL original: {original_url}')

    # TObter as URLs mais acessadas
    most_accessed_urls = get_most_accessed_urls()
    print('Top 10 URLs mais acessadas:')
    for index, url_info in enumerate(most_accessed_urls, start=1):
        print(f'{index}. {url_info["original_url"]} - Acessos: {url_info["access_count"]}')
