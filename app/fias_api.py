import requests
from app import config

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Token ' + config.DADATA_TOKEN
}

def make_request(url, data):
  r = requests.post(url, headers=headers, data=data.encode('utf8'))
  return r.json()

def suggest(query, count = 10):
  url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'
  data = '{ "query": "' + query + '", "count": ' + str(count) + ' }'
  return make_request(url, data)

def currency(query):
  url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/currency'
  data = '{ "query": "' + query + '" }'
  return make_request(url, data)