import requests
import re

def send_telegram(token, chat_id, msg):
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat_id, "text": msg}
    )

def extract_price(text):
    prices = re.findall(r"\d{2,4}[,.]\d{2}", text)

    clean = []
    for p in prices:
        try:
            clean.append(float(p.replace(".", "").replace(",", ".")))
        except:
            pass

    return min(clean) if clean else None