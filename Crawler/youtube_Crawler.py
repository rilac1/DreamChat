import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scraper(id):
  #colab이 gui환경을 제공하지 않으므로 이하 옵션이 없으면 
  #DevToolsActivePort file doesn't exist 오류발생
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev')

  #설치된 크롬드라이버의 경로 입력
  driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)

  #추후 구동환경에따라 수정 필요
  browser = webdriver.Chrome(chrome_options=options)

  url = "https://www.youtube.com/live_chat?v=" + str(id)
  browser.get(url)
  browser.implicitly_wait(1)
  #innerHTML = browser.execute_script("return document.body.innerHTML")
  chats = []
  for chat in browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):
    time = chat.find_element_by_css_selector("#timestamp").get_attribute('innerHTML')
    author_name = chat.find_element_by_css_selector("#author-name").get_attribute('innerHTML')
    message = chat.find_element_by_css_selector("#message").get_attribute('innerHTML')
	  #author_name_encoded = author_name.encode('utf-8').strip()
	  #message_encoded = message.encode('utf-8').strip()
    obj = json.dumps({'time': time, 'author_name': author_name, 'message': message})
    chats.append(json.loads(obj))

  browser.quit()
	#display.stop()
	#vdisplay.stop()
  return chats
