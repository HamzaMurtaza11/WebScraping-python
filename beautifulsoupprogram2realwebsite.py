from bs4 import BeautifulSoup
import requests

html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

#print(html_text)

soup= BeautifulSoup(html_text,"lxml")
#print(soup.prettify())

jobs= soup.find_all("li",class_="clearfix job-bx wht-shd-bx")


for job in jobs:
    with open ("scraped_data.txt","a+") as f:
       company_name=job.find("h3",class_="joblist-comp-name").text.replace(' ','')
       f.write("COMPANY NAME:"+company_name.strip()+"\n")
       skills=job.find("span",class_="srp-skills").text.replace(' ','')
       f.write("SKILLS:"+skills.strip()+"\n")
       more_info=job.header.h2.a['href']
       f.write("MORE INFORMATION:" + more_info.strip()+"\n")


    











  