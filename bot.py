# import logging
import json

from pyrogram import Client

from data import whispers

api_id = 11144788
api_hash = "fc82681ae36d60a860633f42252a54d8"

app = Client("5695443548:AAG0I0wombUTOO9FeOh8hpWYKv4WR3Xg2dg", api_id=api_id, api_hash=api_hash)

plugins = dict(
    root="plugins",
    include=[
        "inline",
        "private"
    ]
)

# logging.basicConfig(level=logging.DEBUG)
print('>>> BOT STARTED')
Client("ezWhisperBot", plugins=plugins).run()
with open('data.json', 'w') as f:
    json.dump(whispers, f)
print('\n>>> BOT STOPPED')
