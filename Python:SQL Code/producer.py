import requests 
import re
from kafka import KafkaProducer
from time import sleep
from json import dumps


while True:


    producer = KafkaProducer(bootstrap_servers = "localhost", value_serializer=lambda x: 
                             dumps(x).encode("utf-8"))

    producer2 = KafkaProducer(bootstrap_servers = "18.207.233.150", value_serializer=lambda x: 
                             dumps(x).encode("utf-8"))


    TOPIC = "flight_data"

    # # get flight data 

    params = {
    "access_key": "a092628744f8f369c74e42b6446a2010",
    "flight_status": "landed",
    "flight_date": "2023-04-17",
    "arr_icao" : "KBOS", # FLIGHTS ONLY ENTERING BOSTON
    "sort": "flight_date"}
    

    api_result = requests.get("http://api.aviationstack.com/v1/flights", params)

    api_response = api_result.json()

    for i, flight in enumerate(api_response["data"]):
            
            try:
                
                #APPEND ALL DATA TO A DICT VARIABLE
                dct = flight

                # # COLLECT WEATHER DATA...

                # # extracting country for weather data
                zone = flight["arrival"]["timezone"]
                pattern = r"/(.*)"
                match = re.search(pattern, zone)
                res = match.group(1)

                params_weather = {
                "access_key": "4b8513b181cd2031c208e116665d4efa",
                "query": str(res)
                }

                weather_result = requests.get("http://api.weatherstack.com/current", params_weather)

                api_response2 = weather_result.json()

                dct["destination"] = api_response2["location"]["name"]
                dct["country"] = api_response2["location"]["country"]
                dct["arrival_airport"] = flight["arrival"]["airport"]
                dct["schedule_arrive"] = flight["arrival"]["scheduled"]
                dct["airline"] = flight["airline"]["name"]
                
                dct["temperature"] = api_response2["current"]["temperature"]
                dct["description"] = api_response2["current"]["weather_descriptions"]
                dct["wind_speed"] = api_response2["current"]["wind_speed"]
                dct["wind_degree"] = api_response2["current"]["wind_degree"]
                dct["humidity"] = api_response2["current"]["humidity"] 
                dct["feelslike"] = api_response2["current"]["feelslike"]
                dct["visibility"] = api_response2["current"]["visibility"]
                dct["cloud_cover"] = api_response2["current"]["cloudcover"]

                # # GET AIRLINE DATA

                airline = flight["airline"]

                params = {"access_key" : "a092628744f8f369c74e42b6446a2010",
                          "search" : airline}
                
                airline_result = requests.get(f"https://api.aviationstack.com/v1/airlines", params = params)

                api_response4 = airline_result.json()

                # # UPDATE DICT WITH AIRLINE DATA

                try:
                     
                     dct.update((api_response4["data"][0]))

                except:
                     dct.update((api_response4["data"][1]))
                     

                # # GET COUNTRY DATA 

                country = dct["country_name"]

                country_params = {
                        "access_key" : "a092628744f8f369c74e42b6446a2010",
                        "search" : str(country)}


                country_result = requests.get("https://api.aviationstack.com/v1/countries", params = country_params)

                api_response5 = country_result.json()


                # #UPDATE DICT WITH COUNTRY DATA

                try: 
                     dct.update((api_response5["data"][0]))
                
                except:
                     dct.update((api_response5["data"][1]))

                try:
  
                    airplane = flight["aircraft"]["registration"]


                    airplane_param = {"access_key" :"a092628744f8f369c74e42b6446a2010",
                                    "search": str(airplane)}
                    
                    airplane_response = requests.get("https://api.aviationstack.com/v1/airplanes", params = airplane_param)

                    api_response6 = airplane_response.json()

                    dct.update((api_response6["data"][0]))
                
                except:
                     pass


                producer.send(TOPIC, value = dct)


                sleep(3)


            except Exception as e:
                 print("didnt work:", e)
                 pass

     
    