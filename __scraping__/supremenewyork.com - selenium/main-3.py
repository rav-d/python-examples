
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.15
#
# title: Cant get bot to select item off of supreme
# url: https://stackoverflow.com/questions/70357602/cant-get-bot-to-select-item-off-of-supreme/70358267#70358267

# [Cant get bot to select item off of supreme](https://stackoverflow.com/questions/70357602/cant-get-bot-to-select-item-off-of-supreme/70358267#70358267)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Safari()
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.supremenewyork.com/shop/all"
driver.get(url)

#print(driver.page_source)

click = driver.find_element(By.XPATH, '//*[@id="nav-categories"]/li[10]/a')
click.click()

try:
    all_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Boxer Briefs"))
    )
    for element in all_elements:
        print(element.text)
except Exception as ex:
    print('Exception:', ex)

#driver.close()

