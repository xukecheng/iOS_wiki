import requests
from bs4 import BeautifulSoup
import html2text

# 在 https://fatbobman.com/zh/posts/ 查看所有 class 含有 flex-col 的元素
url = "https://fatbobman.com/zh/posts/"
response = requests.get(url)
response.encoding = "utf-8"  # Specify the encoding
soup = BeautifulSoup(response.text, "html.parser")
flex_col_elements = soup.find_all(class_="cursor-pointer")

blog = {}

for element in flex_col_elements:
    blog[element.contents[0].text.strip().replace("/", "-")] = (
        f"https://fatbobman.com{element['href']}"
    )


def get_blog_content(url: str) -> str:
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    # 输出原始 html
    return soup.find("article", class_="prose").prettify()  # type: ignore


for title, url in blog.items():
    # 判断 title 对应的文件是否已经存在，如果存在则跳过
    try:
        with open(
            f"Blog/fatbobman/markdown/{title}.md",
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
        f"Blog/fatbobman/markdown/{title}.md",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(markdown)
