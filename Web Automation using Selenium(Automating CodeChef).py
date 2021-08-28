#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver


# In[23]:


browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")


# In[24]:


browser.get("https://codechef.com")


# In[25]:


username_element=browser.find_element_by_id("edit-name")


# In[26]:


username_element.send_keys("runwalakshat5")


# In[27]:


from getpass import getpass


# In[28]:


password_element=browser.find_element_by_id("edit-pass")


# In[29]:


password_element.send_keys(getpass("Enter password: "))


# In[44]:


browser.get("https://codechef.com/submit/TEST")


# In[43]:


browser.find_element_by_id("edit-submit").click()


# In[50]:


browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# In[51]:


with open("app.py","r") as f:
    code=f.read()


# In[52]:


code_element=browser.find_element_by_id("edit-program")


# In[53]:


code_element.send_keys(code)


# In[61]:


browser.find_element_by_xpath('//*[@id="edit-language"]/option[4]').click()


# In[55]:


browser.find_element_by_id("edit-submit-1").click()


# In[ ]:




