from pprint import pprint
import requests
 #This class is responsible for talking to the Google Sheet.
SHEET_URL = "https://api.sheety.co/c92a271ff04e115f3c611d2bca7b97db/flightDeals/prices"
class DataManager:
    
    def __init__(self):
        self.flights_data = {}
    
    def get_prices(self):
        response = requests.get(url=SHEET_URL)
        data = response.json()

        self.flights_data = data["prices"]
        # pprint(response.json())
        return self.flights_data
    
    
    def get_locations(self):
        for city in self.flights_data:
            parameters = {
                        "price": {
                        "iataCode": city["iataCode"]    }
                        }
            
        response = requests.put(url=f"{SHEET_URL}/{city['id']}",json=parameters)
        print(response.text)
        
    # def delete_testing():
            
    #     pprint(response.text)
    


# response = requests.get(url=SHEET_URL)
# data = response.json()["prices"]
# for city in data:
#     parameters = {
#                 "price": {
#                 "iataCode": city["iataCode"]}
#                 }
#     response = requests.put(url=f"{SHEET_URL}/{city['id']}",json=parameters)
#     data2= response.json()
#     print(response.json())
#     if data2["price"]["iataCode"] =="":
        
#         data2["price"]["iataCode"] ="abc"
#         print(data2)

# API_KEY = "gFj7KRzXE8hj5rC-Mm6kA2-mnHxCtgXl"
# API_ENDPOINT = "https://tequila-api.kiwi.com"

# # code_endpoint = "https://tequila-api.kiwi.com/locations/query"        
# # header = {"apikey":API_KEY}
# # paramet = {"term": city_name, "location_types": "city"}
        
# # response = requests.get(url=code_endpoint,headers=header,params=paramet)
# # # print(response.json())
# # location = response.json()["locations"]
        
# # code = location[0]["iataCode"]



# for row in data:
#     # print(row["city"])
#     code_endpoint = "https://tequila-api.kiwi.com/locations/query"        
#     header = {"apikey":API_KEY}
#     paramet = {"term": row["city"], "location_types": "city"}
            
#     response = requests.get(url=code_endpoint,headers=header,params=paramet)
#     # print(response.json())
#     location = response.json()["locations"]
            
#     code = location[0]["code"]
#     print(code)
    
    
    


