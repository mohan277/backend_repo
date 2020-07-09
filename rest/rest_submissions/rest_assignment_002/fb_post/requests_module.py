import requests


# Task 1
# data = '{"user_id":1, "content":"Post1"}'
# url = 'http://127.0.0.1:8000/fb_post/post/'
# response = requests.post(
#     url=url,
#     data=data,
#     headers={'Content-type': 'application/json'}
#     )
# print(response.content)

# Task 2
url = 'http://127.0.0.1:8080/fb_post/post/2/'
response = requests.get(url=url)
print(response.content)

# Task 3
# data = '{"user_id": 1, "content": "Harish_The_Hero"}'
# url = 'http://127.0.0.1:8000/fb_post/comment/2/reply/create/'
# response = requests.post(
#     url=url,
#     data=data,
#     headers={'Content-type': 'application/json'}
#     )
# print(response.content)

# # Task 4
# data = '{"user_id":1,"reaction_type":"WOW"}'
# url = 'http://127.0.0.1:8000/fb_post/post/1/react/'
# response = requests.post(
#     url=url,
#     data=data,
#     headers={'Content-type': 'application/json'}
#     )
# print(response.content)


# # Task 5
# data = '{"user_id":1,"reaction_type":"WOW"}'
# url = 'http://127.0.0.1:8000/fb_post/comment/1/react/'
# response = requests.post(
#     url=url,
#     data=data,
#     headers={'Content-type': 'application/json'}
#     )
# print(response.content)


# # Task 6
# data = '{"user_id":6}'
# url = 'http://127.0.0.1:8000/fb_post/post/6/delete/'
# response = requests.post(
#     url=url,
#     data=data,
#     headers={'Content-type': 'application/json'}
#     )
# print(response.content)


# Task 6
# data = '{"user_id": 2, "content": "Comment"}'
# url = 'http://127.0.0.1:8000/fb_post/post/1/comment/create/'
# response = requests.post(
#     url=url,
#     data=data,
#     headers={'Content-type': 'application/json'}
#     )
# print(response.content)
