import requests
from bs4 import BeautifulSoup

# url = "https://www.ycombinator.com/companies/?batch=W21&batch=S20&industry=B2B%20Software%20and%20Services&industry=Financial%20Technology"

# for getting info off the individual page
url = "https://www.ycombinator.com/companies/nano-technologies"
# url = "https://www.ycombinator.com/companies/meru-com"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1', class_="font-bold")
facts = soup.find('div', class_='facts')  # finds facts about company
founders = soup.find('h3', class_='font-bold')
decrp = soup.find('h3',style="font-size:1.5em;margin-bottom:10px;")
linkd = soup.find('div', class_="highlight-box founder-card")


# print(page.content)

def isolateLocation(facts_text):
    loc_num = facts_text.find("Location")
    return facts_text[loc_num + 9: len(facts_text)]

def isolateLinkedIn(link_text_list):
   found_link =  linkd.find('a', class_='social linkedin')
   return found_link['href']



print("Title: " + title.text)
print("Location: " + isolateLocation(facts.text))
print("Founders: " + founders.text)
print("Description: " + decrp.text)
print("LinkedIn: ", isolateLinkedIn(linkd))
print("\n")

# for a in soup.find_all('a', href=True):
#     print("Found URL: ", a['href'])