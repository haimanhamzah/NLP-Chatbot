#Starting Dataset 

countries = [
     {         
               "country": "United Kingdom",
               "city": "London",
               "price": 2500,
               "airlines": ["British Airlines", "Malaysia Airlines"],
               "duration": "13 Hours",
               "budget": 2000   
     },
     {         
               "country": "Japan",
               "city": "Tokyo",
               "price": 1500,
               "airlines": ["Japan Airlines", "Malaysia Airlines"],
               "duration": "7 Hours",
               "budget": 2500   
     },
     {         
               "country": "Korea",
               "city": "Seoul",
               "price": 1000,
               "airlines": ["Korea Airlines", "Malaysia Airlines"],
               "duration": "6 Hours",
               "budget": 1600  
     }   
]

def content_determination(travel):
               return travel

def document_structuring(travel):
               return {
                    "place": [travel['country'], travel['city']],
                    "money": [travel['price'], travel['budget']],
                    "method_to_travel": [travel['airlines']],
                    "how_long": [travel['duration']]         
               }

def aggregation(structure_travel):
               aggregated_data = {}
               
               aggregated_data["place"] = f"{structure_travel['place'][0]} is the country of {structure_travel['place'][1]}"
               aggregated_data["money"] = f"The price to travel to {structure_travel['place'][0]} from Malaysia is
                                             {structure_travel['money'][0]}. The estimated budget for the trip would be
                                             {structure_travel['money'][1]}"
               aggregated_data["method_to_travel"] = f"The airlines available are {structure_travel['method_to_travel'][0]}"
               aggregated_data["how_long"] = f"The estimated duration of the flight is {structure_travel['how_long'][0]}"