import requests

API_KEY = "gFj7KRzXE8hj5rC-Mm6kA2-mnHxCtgXl"
API_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def flight_code(self,city_name):

        code_endpoint = "https://tequila-api.kiwi.com/locations/query"        
        header = {"apikey":API_KEY}
        paramet = {"term": city_name, "location_types": "city"}
        
        response = requests.get(url=code_endpoint,headers=header,params=paramet)
        # print(response.json())
        location = response.json()["locations"]
        
        code = location[0]["code"]
        return code