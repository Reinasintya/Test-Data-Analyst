# API key: e2788ad5bcfd478698c59d80ad717e1e
# from newsapi import NewsApiClient
# # init
# newsapi = NewsApiClient(api_key = 'e2788ad5bcfd478698c59d80ad717e1e')
# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
# sources='bbc-news,the-verge',
# category='business',
# language='en',
# country='us')

api_key = 'e2788ad5bcfd478698c59d80ad717e1e'
kategori = {
    '1': 'technology',
    '2': 'business',
    '3': 'sports',
    '4': 'health',
    '5': 'science'}

print('Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi')
print('[2] Berita seputar bisnis')
print('[3] Berita seputar olahraga')
print('[4] Berita seputar kesehatan')
print('[5] Berita seputar science')

import requests
pilih = input('Cari berita yang Anda inginkan [1/2/3/4/5]: ')
berita = kategori[pilih]

url = 'https://newsapi.org/v2/top-headlines?country=id&category='+berita+'&apiKey='+api_key

articles = requests.get(url)

print('Berikut adalah top 5 berita Indonesia bidang {}:'.format(kategori[pilih]))
i = 0
while i < 5:
    print('{} - {}'.format(i+1, articles.json()['articles'][i]['title']))
    i += 1