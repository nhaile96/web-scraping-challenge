#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
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

    time.sleep(3)

    url='https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[8]:


    art_title=soup.find('div', class_='content_title')
    print(art_title.text)


    # In[10]:


    mars_p= soup.find('div', class_='article_teaser_body')
    print(mars_p.text)


    # # JPL Mars Space Images

    # In[11]:
    browser=init_browser()

    url2="https://spaceimages-mars.com/"
    browser.visit(url2)


    # In[19]:


    html = browser.html
    soup=BeautifulSoup(html,"html.parser")
    img_group=soup.find('div', class_='floating_text_area')

    link=img_group.find('a')
    href=link['href']
    href
    featured_image_url="https://spaceimages-mars.com/" + href
    featured_image_url



    # # Mars Facts

    # In[20]:
    browser=init_browser()

    url3="https://galaxyfacts-mars.com/"


    # In[24]:


    mars_table=pd.read_html(url3)
    mars_table


    # In[23]:


    type(mars_table)


    # In[26]:


    mars_df=mars_table[0]
    html_mars_df = mars_df.to_html()
    html_mars_df
    browser.quit()


    # # Mars Hemispheres

    # In[3]:

    browser=init_browser()
    url4='https://marshemispheres.com/'
    browser.visit(url4)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results=soup.find_all('div', class_='item')
    results


    # In[11]:


    hemisphere_image_urls=[]

    for result in results:
        
        title=result.h3.text

        href=result.find('a')['href']
        image_url="https://marshemispheres.com/" + href
        
        browser.visit(image_url)
        html=browser.html
        soup=BeautifulSoup(html,'html.parser')
        
        downloads= soup.find('div', class_='downloads')
        img_link= downloads.find('a')['href']
        full_url= "https://marshemispheres.com/" + img_link
        
        hemisphere_image_urls.append({'title':title, "image url":full_url})


    # In[12]:
    mars_data={
        "News Title":art_title,
        "News Paragraph": mars_p,
        "Featured Image Url": featured_image_url,
        "Html Table": html_mars_df,
        "Hemisphere Image Urls": hemisphere_image_urls
    }

    browser.quit()
    return mars_data

    if __name__=="__main__":
        print(scrape())
        
    # In[ ]:




