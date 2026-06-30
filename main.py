import os
from utils import send_telegram, extract_price
from sites.unieuro import get_price

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
TARGET = float(os.environ.get("TARGET_PRICE", 900))

PRODUCTS = [
    {
        "name": "MacBook Air M4",
        "url": "https://www.unieuro.it/"
    }
]

for p in PRODUCTS:
    text = get_price(p["url"])
    price = extract_price(text)

    if price:
        print(p["name"], price)

        if price <= TARGET:
            send_telegram(
                TOKEN,
                CHAT_ID,
                f"🔥 OFFERTA!\n{p['name']}\n{price}€\n{p['url']}"
            )