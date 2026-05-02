from yandex_music import Client
import os

from dotenv import load_dotenv

load_dotenv()

client = Client(os.environ.get('YANDEX_ACCESS_TOKEN')).init()

print(client.users_likes_tracks()[0].fetch_track())
