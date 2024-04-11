import requests
from bs4 import BeautifulSoup
import html2text

url = "https://swiftwithmajid.com/archive/"
response = requests.get(url)
response.encoding = "utf-8"  # Specify the encoding
soup = BeautifulSoup(response.text, "html.parser")
li_elements = soup.find_all("li")

blog = {}

for element in li_elements:
    blog[element.contents[1].contents[3]["title"].replace("/", "-")] = (
        f"https://swiftwithmajid.com{element.contents[1].contents[3]['href']}"
    )


def get_blog_content(url: str) -> str:
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    # 输出原始 html
    return soup.find("article").prettify()  # type: ignore


for title, url in blog.items():
    # 判断 title 对应的文件是否已经存在，如果存在则跳过
    try:
        with open(
            f"Blog/swiftwithmajid/markdown/{title}.md",
            "r",
            encoding="utf-8",
        ) as f:
            continue
    except FileNotFoundError:
        pass
    html = get_blog_content(url)
    h = html2text.HTML2Text()
    markdown = h.handle(html)
    # 保存为 markdown 文件
    with open(
        f"Blog/swiftwithmajid/markdown/{title}.md",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(markdown)
