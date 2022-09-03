# import logging
import json

from pyrogram import Client

from data import whispers

app = Client(
     "Whisper-Bot",
    api_id,
    api_hash,
    bot_token,
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
