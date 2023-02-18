# import logging
import json

from pyrogram import filters, Client

from data import whispers

api_id = 1714588
api_hash = "78c27bf90c81f15a8af4aa0aeeadfc42"
bot_token = "6026914511:AAHBYpcI9M9nc6QOaKpkanR7SLuKZnqITRU"

plugins = dict(
    root="plugins",
    include=[
        "inline",
        "private"
    ]
)

# logging.basicConfig(level=logging.DEBUG)
print('>>> BOT STARTED')
Client("ezWhisperBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token, plugins=plugins).run()
with open('data.json', 'w') as f:
    json.dump(whispers, f)
print('\n>>> BOT STOPPED')
