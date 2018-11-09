import requests

BLOG_RANKING_ID1 = '1970869'
BLOG_RANKING_ID2 = '1530241125'

api = "http://blog.with2.net/ping.php/{id1}/{id2}"

# APIのURL作成
url = api.format(id1=BLOG_RANKING_ID1, id2=BLOG_RANKING_ID2)

# 実際にAPIにリクエストを送信して結果を取得する
r = requests.get(url)

print(r)
