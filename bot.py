# import logging
import json

from pyrogram import Client

from data import whispers

app = Client(
     "Whisper-Bot",
    api_id= 11523090,
    api_hash="a27541e538e3e1fb05e90297d9140330",
    bot_token="5410459821:AAFppkpzMGph6MKlIiNF5RJr6DGXdR7Ryt0",
    plugins = dict(
    root="plugins",
    include=[
        "inline",
        "private"
    ]
))

# logging.basicConfig(level=logging.DEBUG)
print('>>> BOT STARTED')
Client("ezWhisperBot", plugins=plugins).run()
with open('data.json', 'w') as f:
    json.dump(whispers, f)
print('\n>>> BOT STOPPED')
