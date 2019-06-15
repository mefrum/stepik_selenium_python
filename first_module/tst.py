import time

from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
# Ваш код, который заполняет обязательные поля
first_block_elements = browser.find_elements_by_css_selector('.first_block > div')
second_block_elements = browser.find_elements_by_css_selector('.second_block > div')
for element in first_block_elements:
    element.find_element_by_css_selector('input').send_keys('value')

for element in second_block_elements:
    element.find_element_by_css_selector('input').send_keys('value')
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
# Проверяем, что смогли зарегистрироваться
#  ждем загрузки страницы
time.sleep(1)
# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
