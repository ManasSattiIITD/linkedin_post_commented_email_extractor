from selenium import webdriver
import time
import re
import pandas as pd
browser = webdriver.Chrome("C:\development\chromedriver.exe")
time.sleep(2)
post_url = "LINKEDIN_POST_URL"
browser.get(post_url)
username = "your username"
password = "your password"
apple = browser.find_elements_by_class_name("public-post__social-counts-item") 
time.sleep(1)
apple[0].click()
browser.find_element_by_id("username").send_keys(username)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_class_name("btn__primary--large").click()
more_comments_button = browser.find_element_by_class_name("comments-comments-list__show-previous-button")
while(len(more_comments_button) != 0)
    time.sleep(1.5)
    more_comments_button.click()
    time.sleep(1)
more_comments_button = browser.find_element_by_class_name("comments-comments-list__show-previous-button")
while(len(more_comments_button) != 0)
    time.sleep(1.5)
    more_comments_button.click()
    time.sleep(1)
mail_list = re.findall(r'\w+@\w+\.{1}\w+', page_source)
try:
    df = pd.read_csv('linkedin_posts_emails.csv')
    print("File found.")
    df = pd.DataFrame(mail_list, columns = [post_url])
    df.insert(0,post_url,mail_list,allow_duplicates =  True)
    df.to_csv('linkedin_posts_emails.csv')
    print("Task Done")
except FileNotFoundError:
    print("File didn't exists! Creating File.")
    open('linkedin_posts_emails.csv',mode='w')
    df = pd.DataFrame(mail_list, columns = [post_url])
    df.to_csv('linkedin_posts_emails.csv')
    print("Task Done")