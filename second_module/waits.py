import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element(
        (By.ID, "price"), "10000 RUR")
)
browser.find_element_by_css_selector("#book").click()

found_x = browser.find_element_by_css_selector("#input_value").text
x = calc(int(found_x))
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_css_selector("#solve").click()
