from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_searching = FlightSearch()

excel_data = data_manager.get_prices()


if excel_data[0]["iataCode"] == "":
    for row in excel_data:
        row["iataCode"] = flight_searching.flight_code(row["city"])
        print(f"excel_data:\n {excel_data}")
    data_manager.flights_data = excel_data
    data_manager.get_locations()