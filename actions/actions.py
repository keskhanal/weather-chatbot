import os, requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

WEATHER_API_KEY = "WEATHER_API_KEY"


class ActionWeather(Action):
  def name(self) -> Text:
    return "action_weather"

  def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:   
    loc = tracker.get_slot('GPE')
    print(loc)
    degree_sign= u'\N{DEGREE SIGN}'
    
    payload = {'q': loc, 'units': 'metric', 'appid': WEATHER_API_KEY}
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    
    try:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        city = data['name']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        clouds = data['clouds']['all']
        
        weather_data = """It is {}{}C in {}. The humidity is {}%, wind speed is {} meter/sec, cloudiness in the sky is {}%, and it is {} at the moment.""".format(temp, degree_sign,city, humidity, wind_speed, clouds, desc)
        dispatcher.utter_message(weather_data)

        return [SlotSet("GPE", None)]

    except requests.exceptions.HTTPError as e:
      dispatcher.utter_message(text="City not found!")

    except Exception as e:
      dispatcher.utter_message(text="Could not find the city!")


class ActionFeedback(Action):
  def name(self) -> Text:
    return "action_feedback"

  def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:    
    intent = tracker.get_intent_of_latest_message()
  

    if intent == "affirm":
      return [SlotSet('feedback', True)]

    elif intent == "deny":
      return [SlotSet('feedback', False)]

    return []

