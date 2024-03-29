import os

from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'tst.txt')  # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_name("firstname").send_keys("first_name")
browser.find_element_by_name("lastname").send_keys("last_name")
browser.find_element_by_name("email").send_keys("last_name")
browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)
browser.find_element_by_css_selector("button.btn").click()
