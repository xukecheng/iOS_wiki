import requests
import json
import os
import html2text

BROWSERLESS_URL = os.environ.get("BROWSERLESS_URL")
BROWSERLESS_TOKEN = os.environ.get("BROWSERLESS_TOKEN")

r = requests.get(
    "https://developer.apple.com/tutorials/data/index/appstoreservernotifications"
)
print(r.status_code)

json_data = json.loads(r.text)
print(json_data)

swiftUI = json_data["interfaceLanguages"]["data"][0]["children"]


def get_data(swiftUI: list, title=None):
    for item in swiftUI:
        if (
            item["type"] == "overview"
            or item["type"] == "sampleCode"
            or item["type"] == "groupMarker"
            or item["title"] == "SceneBuilder"
            or "accessibility" in item["title"]
        ):
            continue
        if "children" in item:
            get_data(item["children"], item["title"])
        else:
            if title:
                if title not in urls:
                    urls[title] = []
                urls[title].append(item)


urls = {}
get_data(swiftUI)


def get_url_markdown(path: str) -> str:
    scrape_url = f"https://developer.apple.com{path}"
    request_url = f"{BROWSERLESS_URL}/scrape?token={BROWSERLESS_TOKEN}"
    print(scrape_url)
    body = {
        "url": scrape_url,
        "elements": [{"selector": "main"}],
    }
    r = requests.post(request_url, json=body)
    r.encoding = "utf-8"
    scrape_data = json.loads(r.text)
    html = scrape_data["data"][0]["results"][0]["html"]
    h = html2text.HTML2Text()
    h.ignore_images = True
    h.ignore_links = True
    markdown = h.handle(html)
    return markdown


for key, value in urls.items():
    try:
        with open(
            f"Documentation/AppStoreServerNotifications/Documentation/{key}.md",
            "r",
            encoding="utf-8",
        ) as f:
            continue
    except FileNotFoundError:
        pass
    markdown = ""
    for item in value:
        path = item["path"]
        markdown += get_url_markdown(path)
    with open(
        f"Documentation/AppStoreServerNotifications/Documentation/{key}.md",
        "w",
    ) as f:
        f.write(markdown)
