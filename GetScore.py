from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Grid import Grid


# ------------------------------------------------------------------------------------------
# ACCESO A 2048 ORIGINAL

url = 'https://play2048.co'
driver = webdriver.Chrome('/Users/David/Desktop/chromedriver')
driver.get(url)
body = driver.find_element_by_tag_name('body')

for i in range(35):
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)
    body.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.1)

html = driver.page_source
time.sleep(2)
here = html.index('"score-container"')
her = html[here+18:here+25]
print(her)
score=''

for character in her:
    if character.isdigit():
        score+=character

print(score)