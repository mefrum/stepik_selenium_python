from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_name("first_name").send_keys("first_name")
browser.find_element_by_name("last_name").send_keys("last_name")
browser.find_element_by_class_name("city").send_keys("city")
browser.find_element_by_id("country").send_keys("country")

browser.find_element_by_css_selector("button.btn").click()
