from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

browser.get(link)

x = browser.find_element_by_css_selector("#num1").text
y = browser.find_element_by_css_selector("#num2").text
value = int(x) + int(y)
select = Select(browser.find_element_by_css_selector("#dropdown"))
select.select_by_value(str(value))
browser.find_element_by_css_selector("button.btn").click()
