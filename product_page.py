# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_added_to_basket(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text
        message = self.browser.find_element(By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong").text
        assert product_name == message, "Product name in message is incorrect"

    def should_be_correct_basket_price(self):
        product_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text
        basket_price = self.browser.find_element(By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner strong").text
        assert product_price == basket_price, "Basket price is incorrect"