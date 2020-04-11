import requests
import time
from bs4 import BeautifulSoup

url_categories = [
    "https://www.filipeflop.com/categoria/arduino/",
    "https://www.filipeflop.com/categoria/campanha_natal_filipeflop/",
    "https://www.filipeflop.com/categoria/componentes-eletronicos/",
    "https://www.filipeflop.com/categoria/display-e-iluminacao/",
    "https://www.filipeflop.com/categoria/impressao-3d/",
    "https://www.filipeflop.com/categoria/livros/",
    "https://www.filipeflop.com/categoria/modulos/",
    "https://www.filipeflop.com/categoria/outlet/",
    "https://www.filipeflop.com/categoria/partes/",
    "https://www.filipeflop.com/categoria/placas-de-desenvolvimento/",
    "https://www.filipeflop.com/categoria/prototipagem/",
    "https://www.filipeflop.com/categoria/raspberry-pi/",
    "https://www.filipeflop.com/categoria/robotica/",
    "https://www.filipeflop.com/categoria/sensores/",
    "https://www.filipeflop.com/categoria/teste-e-medicao/",
    "https://www.filipeflop.com/categoria/wearable/",
    "https://www.filipeflop.com/categoria/wireless-e-iot/"
]
url_regulamento = "https://www.filipeflop.com/regulamento/"

start_time = time.time()

eggs_urls = []
for category_url in url_categories:
    data = {'ppp': -1}      # Products Per Page, -1 means no limits
    category_page = requests.get(category_url, data)
    soup = BeautifulSoup(category_page.content, 'html.parser')
    itens = soup.find_all('div', class_='product-loop-header product-item__header')
    for i in itens:
        prod_url = i.contents[1].attrs['href']
        prod_page = requests.get(prod_url)
        soup_prod = BeautifulSoup(prod_page.content, 'html.parser')
        div_prod_summary = soup_prod.find_all('div',class_='summary entry-summary')
        # looking for this URL, that means an easter egg
        if len(div_prod_summary[0].findAll(href = url_regulamento)) > 0: 
            print(prod_url)
            eggs_urls.append(prod_url + "\n")

u_eggs_urls = set(eggs_urls)      # converting to set and removind duplicates

with open("eggs_filipeflop.txt", "w") as f:
    f.writelines(u_eggs_urls)
    end_time = time.time()
    f.write("\n Elapsed time : " + str(end_time - start_time) + " seconds")

end_time = time.time()

print("Elapsed time : " + str(end_time - start_time) + " seconds")