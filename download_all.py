import os
from dotenv import load_dotenv
from fetch_apod_images import download_apod_pics
from fetch_epic_images import download_epic_pics
from fetch_spacex_images import fetch_spacex_launch

SPACEX_IDS = ['6243adcaaf52800c6e919254', '61e048bbbe8d8b66799018d0']

load_dotenv()
nasa_token = os.environ['NASA_TOKEN']
for id in SPACEX_IDS:
    fetch_spacex_launch(id)
download_apod_pics(nasa_token, 30)
download_epic_pics(nasa_token, date='2023-01-10')
print('All photos are downloaded')
