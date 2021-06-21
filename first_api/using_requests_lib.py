import requests

r_post = requests.post('http://127.0.0.1:5000/sum_body', json={"valores": [10,20,30]})
j_post = r_post.json()
print("post result | ", j_post)

r_get = requests.get('http://127.0.0.1:5000/sum_body')
j_get = r_get.json()
print("get result | ", j_get)