import time

import calc as calc
def calc(x):
 return str(math.log(abs(12 * math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
x = x_element.text
y = calc(x)
input = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
input.send_keys(y)
option1 = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
option2.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(5)