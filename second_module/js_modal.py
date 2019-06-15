import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector(".btn.btn-primary").click()
confirm = browser.switch_to.alert
confirm.accept()

found_x = browser.find_element_by_css_selector("#input_value").text
x = calc(int(found_x))
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_css_selector("button.btn").click()
