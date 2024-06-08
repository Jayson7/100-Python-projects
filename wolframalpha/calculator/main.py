app_id = 'b9f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8'
import wolframalpha
# import requests
# create a calculator app
client = wolframalpha.Client(app_id)
# get the result
result = client.query('what is the meaning of meteorology') 
# print the result in a readable format
for pod in result.pods:
    for sub in pod.subpods:
        print(sub.plaintext)
            
    
