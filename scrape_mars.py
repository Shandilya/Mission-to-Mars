from bs4 import BeautifulSoup
from jinja2 import Template, StrictUndefined
from urllib.request import urlopen as ureq
import requests
from splinter import Browser
import time
import pandas as pd

# def init_browser():
executable_path = {"executable_path":"chromedriver.exe"}
browser =  Browser("chrome", **executable_path, headless=False)

# Mars News
def scrape():
        # browser= init_browser()
        listings_news = {}

        url ="https://mars.nasa.gov/news/"
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html,"html.parser")

        print(soup.prettify())

        listings_news["news_title"] = soup.find("div", class_="content_title").find("a").get_text()
        listings_news["news_p"] = soup.find("div", class_="article_teaser_body").get_text()
        listings_news["news_date"] = soup.find("div", class_="list_date").get_text()
        print(listings_news["news_title"])
        print(listings_news["news_p"])
        print(listings_news["news_date"])
        # return listings_news
     
#  JPL Mars Space

        url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_image)
        browser.click_link_by_partial_text('FULL IMAGE')
        time.sleep(5)
        browser.click_link_by_partial_text('more info')
        time.sleep(5)
        html1 = browser.html
        soup1 = BeautifulSoup(html1, 'html.parser')
        extension = soup1.find("article").find("figure", class_="lede").a["href"]
        link = "https://www.jpl.nasa.gov"
        featured_image_url = link + extension
        print(featured_image_url)
        listings_news["featured_image_url"]


# Mars Weather


        url1 ="https://twitter.com/marswxreport?lang=en"
        browser.visit(url1)
        ht = browser.html
        # response = requests.get(url)
        soup2 = BeautifulSoup(ht, 'html.parser')
        listings_news["mars_weather"] = soup2.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        print(listings_news["mars_weather"])
        
# Mars Fact
        url2 ="http://space-facts.com/mars/"
        browser.visit(url2)
        response = browser.html
        soup3 = BeautifulSoup(response, 'html.parser')

        table_data = soup.find('table', class_="tablepress tablepress-id-mars")
        table_all = table_data.find_all('tr')
        labels = []
        values = []
        for tr in table_all:
                td_elements = tr.find_all('td')
                labels.append(td_elements[0].text)
                values.append(td_elements[1].text)
                mars_facts_df = pd.DataFrame({
                "Label": labels,
                "Values": values
                })  
        fact_table = mars_facts_df.to_html(header = False, index = False)
        fact_table
        mars_profile = {}
        table = pd.read_html(url)
        print(table[0])
        df_mars_facts = table[0]
        df_mars_facts.columns=["Description", "Value"]
        df_mars_facts.set_index(["Description"])
        html_table=df_mars_facts.to_html()
        print(scrape())
# 5 -  Mars Hemispheres.  URL of page to be scraped
# 5.1 Working on Cerberus Hemisphere Enhanced
        # executable_path = {"executable_path":"C:/Users/Deepti/Washu BootCamp - HW/Mission-to-Mars/chromedriver"}
        # browser = Browser('chrome', **executable_path, headless=False)
        url5 ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        # Empty list of image urls
        hemisphere_image_urls = []
        # Scraping
        browser.visit(url5)
        time.sleep(5)
        browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
        time.sleep(5)
        html5 = browser.html
        soup5 = BeautifulSoup(html5, 'html.parser')
        cerberus_link = soup5.find("div", class_="downloads").a["href"]
        print(cerberus_link)
        Create dictionary
        cerberus = {
        "title": "Cerberus Hemisphere Enhanced",
        "img_url": cerberus_link
        }
        Appending dictionary
        hemisphere_image_urls.append(cerberus)


# 5.2 Working on Schiaparelli Hemisphere Enhanced
        executable_path = {"executable_path":"C:/Users/Deepti/Washu BootCamp - HW/Mission-to-Mars/chromedriver"}
        browser = Browser('chrome', **executable_path, headless=False)
        url6 ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        # Scraping
        browser.visit(url6)
        time.sleep(5)
        browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
        time.sleep(5)
        html6 = browser.html
        soup6 = BeautifulSoup(html6, 'html.parser')
        schiaparelli_link = soup6.find("div", class_="downloads").a["href"]
        print(schiaparelli_link)
        Create dictionary
        schiaparelli = {
        "title": "Schiaparelli Hemisphere Enhanced",
        "img_url": schiaparelli_link
        }
        # Appending dictionary
        hemisphere_image_urls.append(schiaparelli)

 # 5.3 Working on Syrtis Major Hemisphere Enhanced

        executable_path = {"executable_path":"C:/Users/Deepti/Washu BootCamp - HW/Mission-to-Mars/chromedriver"}
        browser = Browser('chrome', **executable_path, headless=False)
        url7 ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        # Scraping
        browser.visit(url7)
        time.sleep(5)
        browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
        time.sleep(5)
        html7 = browser.html
        soup7 = BeautifulSoup(html7, 'html.parser')
        syrtis_link = soup7.find("div", class_="downloads").a["href"]
        print(syrtis_link)
        # Create dictionary
        syrtis = {
        "title": "Syrtis Major Hemisphere Enhanced",
        "img_url": syrtis_link
        }
        # Appending dictionary
        # hemisphere_image_urls.append(syrtis)        

# 5.4 Working on Valles Marineris Hemisphere Enhanced
        executable_path = {"executable_path":"C:/Users/Deepti/Washu BootCamp - HW/Mission-to-Mars/chromedriver"}
        browser = Browser('chrome', **executable_path, headless=False)
        url8 ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        # Scraping
        browser.visit(url8)
        time.sleep(5)
        browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
        time.sleep(5)
        html8 = browser.html
        soup8 = BeautifulSoup(html8, 'html.parser')
        valles_link = soup8.find("div", class_="downloads").a["href"]
        print(valles_link)
        Create dictionary
        valles = {
        "title": "Valles Marineris Hemisphere Enhanced",
        "img_url": valles_link
        }
        # Appending dictionary
        # hemisphere_image_urls.append(valles)



