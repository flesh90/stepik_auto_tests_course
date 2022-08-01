import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path=r'C:\Users\admin\Downloads\chromedriver\chromedriver.exe')
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
buttons = browser.find_element(By.ID, "book")
buttons.click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
browser.find_element(By.ID, "solve").click()

time.sleep(3)
browser.quit()



//*[@id="layoutDefault"]/div/main/div/div/div/div[1]/div/div/div[2]
'//*[@class="v-data-table__wrapper"]/table/tbody/tr[1]/td[7]/button/span/i'
//*[@id="layoutDefault"]/div/main/div/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button/span/i