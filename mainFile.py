import extractor
import config
import transform_flights
import loader

#Call to the API 

params = {
    "access_key": config.API_KEY,
    "dep_iata": "DUB",
    #"airline_name" :"Ryanair Ltd.",
    "limit": 10
}
data = []
data = extractor.get("flights",params)
#print("Raw data")
#print(data)

#send and receive the data of transform 
transformed_data = transform_flights.transform_flights(data)
""" print("Transform data")
print(transformed_data[0]) """
loader.save(transformed_data)