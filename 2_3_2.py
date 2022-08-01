import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path=r'C:\Users\admin\Downloads\chromedriver\chromedriver.exe')
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
first_window = browser.window_handles[0]
browser.find_element(By.CLASS_NAME, "trollface").click()
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
browser.find_element(By.CLASS_NAME, "btn ").click()

time.sleep(5)
browser.quit()

