import urllib

from bs4 import BeautifulSoup as soup

# newegg.com
my_url = "https://www.newegg.com/Monitors/Category/ID-19?circle5"

# Opening connection and grabbing the page
uClient = urllib.urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
print(containers[0].div.div.a.img["title"])

# saving it in an excel file
filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    f.write(brand + "," + product_name.replace(",", " |") + "," + shipping + "\n")

f.close()
