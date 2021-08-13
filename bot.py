import json
import requests
from norm import TextNormalizer, WordExtractor, ApplyStemmer
import pickle
import random

hate = ['By respectful', 'Bye-Bye', 'Goodbye', 'Have a good day', 'Stop', 'No hate','Stop bulling','Be polite',
        'Be friendly']
none_hate = ['Thanks', 'Thank you', 'Thanks a lot.', 'Thank you very much', 'Thanks so much',
             'You\'re welcome.',' My pleasure.', 'Glad to help.','Cool','Ok']

class TelegramBot:
    def __init__(self, pipeline_path):
        self.token = "1940672777:AAFXwYJTXztrAkT8pNwnimRnC0h6dtuVelw"
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.pipe = pickle.load(open("pipe.pkl", "rb"))

    def get_updates(self, offset):
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset+1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def send_message(self, msg, chat_id):
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={msg}'
        if msg is not None:
            requests.get(url)
    def chose_reply(self,message, chat_id):
        prediction = self.pipe.predict([message])[0]
        if prediction == 1:
            response = random.choice(hate)
        else:
            response = random.choice(none_hate)
        self.send_message(response,chat_id)

