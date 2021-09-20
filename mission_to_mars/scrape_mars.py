#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



# In[2]:

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[7]:
def scrape():

    browser=init_browser()

 

    url='https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[8]:


    art_title=soup.find('div', class_='content_title').text
    


    # In[10]:


    mars_p= soup.find('div', class_='article_teaser_body').text
    print(art_title.text)
    print(mars_p.text)


    # # JPL Mars Space Images

    # In[11]:
    

    url2="https://spaceimages-mars.com/"
    browser.visit(url2)
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # In[19]:


    html1 = browser.html
    soup2=BeautifulSoup(html1,"html.parser")
    img_group=soup2.find('div', class_='floating_text_area')

    link=img_group.find('a')
    href=link['href']
    featured_image_url="https://spaceimages-mars.com/" + href
    print(featured_image_url)



    # # Mars Facts

    # In[20]:


    url3="https://galaxyfacts-mars.com/"


    # In[24]:


    mars_table=pd.read_html(url3)
    mars_df=mars_table[0]
    mars_df.columns=['Description', 'Value']
    mars_df.set_index('Description',inplace=True)
    with open('mars_df.html','w') as fo:
        mars_df.to_html(fo)

    # # Mars Hemispheres

    # In[3]:

    
    url4='https://marshemispheres.com/'
    browser.visit(url4)
    html3=browser.html
    soup_3 = BeautifulSoup(html3, 'html.parser')

    results=soup_3.find_all('div', class_='item')
    results


    # In[11]:


    hemisphere_image_urls=[]

    for result in results:
        
        title=result.find('h3').text

        href=result.find('a')['href']
        image_url="https://marshemispheres.com/" + href
        
        browser.visit(image_url)
        html4=browser.html
        soup=BeautifulSoup(html4,'html.parser')
        
        downloads= soup.find('div', class_='downloads')
        img_link= downloads.find('a')['href']
        full_url= "https://marshemispheres.com/" + img_link
        
        hemisphere_image_urls.append({'title':title, "image_url":full_url})
    hemisphere_image_urls

    # In[12]:
    mars_data={
        "mars_title":art_title,
        "mars_paragraph": mars_p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_df.to_html(),
        "mars_hemispheres": hemisphere_image_urls
    }

    browser.quit()
    return mars_data

    # In[ ]:




