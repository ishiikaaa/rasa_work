from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionScrapedData(Action):

    def name(self) -> Text:
        return "action_scraped_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker) -> List[Dict[Text, Any]]:
        # Reading the data from the file
        with open('scraped_data.json') as file:
            data = json.load(file)

        # Assuming 'search_item' is an entity in your domain.yaml
        # Get the user's search item from the tracker
        search_item = tracker.get_slot('search_item')

        # Retrieve the data based on the search item
        search_data = data.get(search_item)

        # Send the data to the user
        dispatcher.utter_message(text=f"Search Data: {search_data}")

        return []
