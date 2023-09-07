import requests
import datetime as dt
USERNAME = "msametozmen"
pixela_url = "https://pixe.la/v1/users"
TOKEN="12321sasfas23dscasc12ecsad"
GRAPH = "mygraph1"

pixela_params ={
    "token":TOKEN,
    "username":"msametozmen",
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
    
}
today_time = dt.datetime.now()
# pixela_response = requests.post(url=pixela_url,json=pixela_params)

# print(pixela_response.text)

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

# pixela_graph_response = requests.post(url=pixela_graph_url,json=pixela_graph_params,headers=headers)
# print(pixela_graph_response.text)


post_valu_url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}"

post_valu_params = {
    "date":today_time.strftime("%Y%m%d"),
    "quantity":"9.7"
}

# post_value_response = requests.post(url=post_valu_url,json=post_valu_params,headers=headers)
# print(post_value_response.text)

put_value_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}/{today_time.strftime('%Y%m%d')}"

param = {
    
    "quantity":"2.1"
}

# put_response = requests.put(url=put_value_endpoint,json=param,headers=headers)

delete_value = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}/{today_time.strftime('%Y%m%d')}"
delete_response = requests.delete(url=delete_value,headers=headers)

print(delete_response.text)
