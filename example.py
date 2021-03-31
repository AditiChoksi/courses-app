"""
Example of how to sue the requests module

"""


import requests
import json

def getArticles(author):
    r = requests.get("http://jsonmock.hackerrank.com/api/articles?author=" + author)
    response_json = json.loads(r.text)

    total_pages = response_json['total_pages']
    data = response_json['data']
    titles = []

    for i in range(1, total_pages):
        if i!=1:
            url = "http://jsonmock.hackerrank.com/api/articles?author=" + author + "&pages=" + str(i)
            r = requests.get(url)
