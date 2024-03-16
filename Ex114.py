#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import requests
import urllib3

urllib3.disable_warnings()
url = 'https://www.pudim.com.br/'
try:
    requests.get(url, verify=False)
    print(f'\033[0;34mO site do pudim está acessível com sucesso!\033[m')
except requests.exceptions.ConnectionError:
    print(f'\033[0;31mO site do pudim não está acessível =( \033[m')

