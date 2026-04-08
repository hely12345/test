import requests
url = 'https://newsapi.org/v2/everything?q=tesla&from=2026-01-17&sortBy=publishedAt&apiKey=92c0d13b23774b47a9f0ddc3836c09af'

resp = requests.get(url)
if resp.status_code==200:
    print(resp.json())
    
