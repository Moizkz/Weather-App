import requests 
import json
import dotenv
import os
from dotenv import find_dotenv, load_dotenv

# dotenv_path = find_dotenv
load_dotenv()
API_Key = os.getenv("key")
url = os.getenv("url")

print("WEATHER APP")
city = input("Enter your city : ")

parms = {
    "q" : city,
    "units" : "metric",
    "appid" : API_Key
}


try : 
    response = requests.get(url ,params=parms, timeout=5)
    Weather = response.json()['weather'][0]['main']
    temp = response.json()['main']['temp']
    feel = response.json()['main']['feels_like']
    print("The weather of ",city," is : ",Weather)
    print("The Temperature of ",city," is : ",temp)
    print("Feels like : ", feel)
except requests.exceptions.Timeout:
    print("Internet is slow")
except requests.exceptions.HTTPError:
      print("No city found")
except requests.exceptions.RequestException as e:
        print("The error is ", e)
        print("Internet not working")
