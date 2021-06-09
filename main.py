import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# you have to download a webdriver for this to work (I used chrome)
driver = webdriver.Chrome("/Users/tyarpornsuksant/Downloads/chromedriver")
# url is from yc directory with filters already attached
driver.get("https://www.ycombinator.com/companies/?batch=W21&batch=S20&industry=Virtual%20and%20Augmented%20Reality&industry=Engineering%2C%20Product%20and%20Design&industry=Infrastructure&industry=Retail&industry=Marketing&industry=Supply%20Chain%20and%20Logistics&industry=Human%20Resources&industry=Analytics&industry=Security&industry=Productivity&industry=Banking%20and%20Exchange&industry=Consumer%20Finance&industry=Payments&industry=Credit%20and%20Lending&industry=Insurance&industry=Asset%20Management")

# scroll to bottom to load all companies (code from github), need to interact with js to load
SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# process the raw html
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
company_hrefs = soup.find_all('a', class_="styles-module__company___1UVnl no-hovercard")  # element that houses href links
# print(x['href'])
company_links = []
for elem in company_hrefs: # populates links for requests
    company_links.append(elem['href'])
    # print(elem['href'])
# print(company_links)

url = "https://www.ycombinator.com"
# refines location data
def isolateLocation(facts_text):
    loc_num = facts_text.find("Location")
    return facts_text[loc_num + 9: len(facts_text)]

def isolateLinkedIn(linkd):
    try:
        found_link = linkd.find('a', class_='social linkedin')
        return found_link['href']
    except:
        return "None"


with open('ycinfo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "location", "founder", "description", "linkedin", "website"])
    for link in company_links:
        page = requests.get(url + link)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find('h1', class_="font-bold")  # company title
        facts = soup.find('div', class_='facts')  # location
        founders = soup.find_all('div', class_='font-bold')  # founder (first one)
        decrp = soup.find('h3', style="font-size:1.5em;margin-bottom:10px;")  # description
        linkd = soup.find('div', class_="highlight-box founder-card")  # linkedin
        website = soup.find('a', target="_blank")  # website

        # cleaned data
        clean_ttle = title.text
        clean_loc = isolateLocation(facts.text)
        clean_foun = founders[1].text
        clean_decrp = decrp.text
        clean_linkd = isolateLinkedIn(linkd)
        clean_web = website['href']
        print("Recording " + clean_ttle)
        writer.writerow([clean_ttle, clean_loc, clean_foun,clean_decrp, clean_linkd, clean_web])



