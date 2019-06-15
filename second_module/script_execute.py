import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

found_x = browser.find_element_by_css_selector("#input_value").text
x = calc(int(found_x))
browser.find_element_by_css_selector("#answer").send_keys(x)

check_robot = browser.find_element_by_css_selector('[for="robotCheckbox"]')
radio_robot = browser.find_element_by_css_selector('[for="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", check_robot)
check_robot.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
radio_robot.click()

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
