# app_id = 'b9f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8'
app_id = 'G4UAUE-V7RE7RJX24'
import wolframalpha
# import requests
# create a weather app
client = wolframalpha.Client(app_id)
# get the weather
weather = client.query('weather in lagos')
# print the weather in a readable format
# print(weather)
# print the weather in a readable format
for pods in weather.pods:
            for sub in pods.subpods:
                print(sub.plaintext)
            
    
