import time
import urllib.request
from selenium import webdriver as wd

# TODO - type instagram id, password and keyword to download image
id = ''
pw = ''
keyword = ''

if not keyword.startswith('#'):
    keyword = '#'+keyword

items_in_row = 3
main_url = 'https://www.instagram.com/'

# TODO - download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/ and locate it in same path
driver = wd.Chrome(executable_path='./chromedriver')
driver.get(main_url)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
time.sleep(2)
inputs = driver.find_elements_by_css_selector('input')
inputs[0].send_keys(id)
inputs[1].send_keys(pw)
time.sleep(3)
driver.find_element_by_xpath('//button[contains(text(), "로그인")]').click()
time.sleep(2)
search_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_field.send_keys(keyword)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[1]/span').click()
time.sleep(5)

images = []
for i in range(1, 35):
    row = driver.find_elements_by_xpath(f'//*[@id="react-root"]/section/main/article/div[2]/div/div[1]')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

    for j in range(1, 4):
        img = driver.find_element_by_xpath(
            f'//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[{j}]/a/div[1]/div[1]/img')
        if img:
            urllib.request.urlretrieve(img.get_attribute('src'), f'{(i-1)*3 + j}.png')
