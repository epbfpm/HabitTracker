import requests as r
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
pixela_token = 'gfdiutg89534'
username = 'epbfpm'
quantity = input('Digaê broder. qts pagitas?:')

# ----- TODAY -----
today = datetime.now()

# ----- USER CREATION -----
user_params = {"token": pixela_token, "username": username, "agreeTermsOfService": "yes", "notMinor": "yes", "thanksCode": "ThisIsThanksCode"}
# server = r.post(url=pixela_endpoint, json=user_params)
# print(server.text)

# ----- GRAPH CREATION -----
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

headers = {
    'X-USER-TOKEN': pixela_token
}
graph_params = {
    "id": "test-graph",
    "name": "Reading graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}
# # server = r.post(url=graph_endpoint, headers=headers, json=graph_params)
# # print(server.text)
# x = f'{pixela_endpoint}/{username}/graphs/test-graph'
# print(x)

# ----- PIXEL CREATION -----
pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/test-graph'

pixel_params = {
    "date": today.strftime('%Y%m%d'),
    "quantity": str(quantity),
}
server = r.post(url=pixel_endpoint, headers=headers, json=pixel_params)
print(server.text)

# ----- PIXEL UPDATE -----
# date = 20221218
# pixelup_endpoint = f'{pixela_endpoint}/{username}/graphs/test-graph/{date}'
#
# pixelup_params = {
#     "date": date,
#     "quantity": str(quantity),
# }
# server = r.put(url=pixelup_endpoint, headers=headers, json=pixelup_params)
# print(server.text)

# ----- PIXEL DELETION -----
# date = 20221218
# pixelup_endpoint = f'{pixela_endpoint}/{username}/graphs/test-graph/{date}'
#
# pixelup_params = {
#     "date": date,
#     "quantity": str(quantity),
# }
# server = r.delete(url=pixelup_endpoint, headers=headers)
# print(server.text)