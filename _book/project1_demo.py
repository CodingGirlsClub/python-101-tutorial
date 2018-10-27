import requests
from bs4 import BeautifulSoup

for n in range(1, 101):
    link = f"https://xkcd.com/{n}/"

    print(f"get {link}")
    response = requests.get(link)
    page = BeautifulSoup(response.text, features="lxml")
    image_elements = page.select("#comic > img")
    src = image_elements[0]['src']
    image_link = f"http:{src}"

    print(f"get {image_link}")
    image_response = requests.get(image_link)

    print(f"write file {n}.jpg")
    with open(f"{n}.jpg", "wb") as f:
        f.write(image_response.content)
