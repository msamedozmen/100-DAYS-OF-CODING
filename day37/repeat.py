import requests
import datetime as dt

USERNAME = "msametozmen2"
pixela_url = "https://pixe.la/v1/users"
TOKEN = "ASF1231WFASF23R2"
GRAPH = "mygraph"
today_time = dt.datetime.now()


#Create User
pixela_params = {
    "username":USERNAME,
    "token":TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_url,json=pixela_params)
# print(response.text)


pixela_graph_url= f"https://pixe.la/v1/users/{USERNAME}/graphs"

pixela_graph_params= {
    "id":GRAPH,
    "name":"Coding",
    "unit": "mins",
    "type":"float",
    "color":"ajisai"   
}
headers = {
    "X-USER-TOKEN":TOKEN
}


# response = requests.post(url=pixela_graph_url,headers=headers,json=pixela_graph_params)
# print(response.text)


post_valu_url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}"

post_valu_params = {
    "date":today_time.strftime("%Y%m%d"),
    "quantity":"9.7"
}


response = requests.post(url=post_valu_url,headers=headers,json=post_valu_params)
print(response.text)

