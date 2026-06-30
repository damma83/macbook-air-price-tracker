import os
from utils import send_telegram, extract_price
from sites.unieuro import get_price as get_unieuro
from sites.mediaworld import get_mediaworld_price

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
TARGET = float(os.environ.get("TARGET_PRICE", 900))

PRODUCTS = [
    {
        "name": "MacBook Air M4 (Unieuro)",
        "url": "https://www.unieuro.it/"
    },
    {
        "name": "MacBook Air M4 (MediaWorld)",
        "url": "https://www.mediaworld.it/it/brand/apple/mac/macbook/macbook-air-m4"
    }
]

for p in PRODUCTS:

    if "unieuro" in p["url"]:
        text = get_unieuro(p["url"])
    else:
        text = get_mediaworld_price(p["url"])

    price = extract_price(text)

    if price:
        print(p["name"], price)

        if price <= TARGET:
            send_telegram(
                TOKEN,
                CHAT_ID,
                f"🔥 OFFERTA!\n{p['name']}\n{price}€\n{p['url']}"
            )
