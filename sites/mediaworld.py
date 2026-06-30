from playwright.sync_api import sync_playwright

def get_mediaworld_price(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_timeout(4000)

        # prova selettore prezzo principale
        try:
            price = page.locator("span.value").first.inner_text()
        except:
            text = page.inner_text("body")
            browser.close()
            return text

        browser.close()
        return price
