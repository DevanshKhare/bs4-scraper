import requests
from bs4 import BeautifulSoup, SoupStrainer

def extract_content(website):

    extracted_content = []

    try:
        response = requests.get(website)
        response.raise_for_status()

        main_section = SoupStrainer(class_=lambda class_: class_ in ("wd_title", "hello"))
        soup = BeautifulSoup(response.content, 'html.parser', parse_only=main_section)


        links = soup.find_all("a", href=True)
        all_links = []

        for link in links:
            href=link.get('href')
            all_links.append(href)


        if(all_links.__len__()>0):
            for link in all_links:
                response = requests.get(link)
                response.raise_for_status()

                soup = BeautifulSoup(response.content,"html.parser")
                body=soup.find("body").get_text()
                strippedbody=" ".join(body.split())
                extracted_content.append(strippedbody)


    except requests.exceptions.RequestException as e:
        print(f"Error encountered while fetching content: {e}")


    return extracted_content



websites = ["https://yoursite.com"]

all_content = []

for website in websites:
    content = extract_content(website)
    all_content.extend(content)

