import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

browser.get(link)
found_x = browser.find_element_by_css_selector("#input_value").text
x = calc(int(found_x))
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
browser.find_element_by_css_selector('[for="robotsRule"]').click()
browser.find_element_by_css_selector("button.btn").click()
