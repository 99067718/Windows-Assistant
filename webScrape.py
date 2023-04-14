# from urllib.request import urlopen
# def GetHTML(link):
#     url = link
#     page = urlopen(url)
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#     print(html)
#     title_index = html.find("<path d=\"m6 14 8 8L30 6v8L14 30l-8-8v-8Z\">")
#     start_index = title_index + len("<path d=\"m6 14 8 8L30 6v8L14 30l-8-8v-8Z\">")
#     end_index = html.find("</path>")
#     title = html[start_index:end_index]

import requests
from bs4 import BeautifulSoup

def GetAnswer(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="answers")
    #print(results.prettify())
    job_elements = results.find_all("div", class_="answer js-answer accepted-answer js-accepted-answer")
    for job_element in job_elements:
        checkMark = job_element.find("svg", class_="svg-icon iconCheckmarkLg")
        # print(title_element.text.strip())
        # print(company_element.text.strip())
        # print(location_element.text.strip())
        # print()
        #print(python_jobs)
    python_job_elements = [
        p_element for p_element in job_elements
    ]
    for job_element in python_job_elements:
        # -- snip -- #
        labels = job_element.find_all("p")
        for textLabel in labels:
            Text = textLabel.getText()
            print(f"Answer: {Text}\n")

GetAnswer("https://stackoverflow.com/questions/41342609/the-difference-between-comparison-to-np-nan-and-isnull")