# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

import requests
import json
from requests.adapters import HTTPAdapter
import io

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=1))

def Request(ing):
    try:
        with open('proxy.txt') as proxies:
            for line in proxies:
                proxy=json.loads(line)
            line = "https://recipe-recommender.herokuapp.com/recommender?ingredients=tomato,lettuce"
            url=line.rstrip()
            data=requests.get(url, proxies=proxy).content
            rawData = json.load(io.StringIO(data.decode('utf-8')))
            return rawData["data"][0]["name"]
    except:
        return "Error en la entrada de datos"

class action_recomendar(Action):

    def name(self) -> Text:
        return "action_recomendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=Request("tomateo,lettuce"))
        return []

