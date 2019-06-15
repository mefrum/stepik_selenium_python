from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()

browser.get(link)

inputs = browser.find_elements_by_tag_name("input")

for inp in inputs:
    inp.send_keys("123")

browser.find_element_by_css_selector("button.btn").click()
