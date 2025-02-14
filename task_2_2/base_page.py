from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random

class BasePage:

    fake = Faker()

    ITEM_CARD = ("xpath", "//div[@class='css-1s2t5t1']")
    ITEM_PICTURE = ("xpath", "//div[@class= 'css-1s2t5t1']/img")
    ITEM_NAME = ("xpath", "//div[@class= 'css-1s2t5t1']//h4")
    ITEM_PRICE = ("xpath", "//div[@class= 'css-1s2t5t1']/div/div[2]")
    CREATING_ITEM_FORM = ("xpath", "//section[@role = 'dialog']")
    CREATE_BUTTON = ("xpath", "//button[text() = 'Создать']")
    NAME_ITEM_FIELD = ("xpath", "//input[@placeholder = 'Название']")
    PRICE_ITEM_FIELD = ("xpath", "//input[@placeholder = 'Цена']")
    DESCRIPTION_ITEM_FIELD = ("xpath", "//input[@placeholder = 'Описание']") 
    LINK_PICTURE_ITEM_FIELD = ("xpath", "//input[@placeholder = 'URL изображения']")
    OADED_PICTURE = ("xpath", "//img[@alt = 'Загруженное изображение']")
    SAVE_ITEM_BUTTON = ("xpath", "//button[text() = 'Сохранить']")
    NECESSARY_ITEM_FIELD_MESSAGE = ("xpath", "//div[text() = 'Поле обязательно для заполнения.']")
    FIND_FIELD = ("xpath", "//input[@placeholder = 'Поиск по объявлениям']")
    FIND_BUTTON = ("xpath", "//button[text() = 'Найти']")
    EDIT_ITEM_BUTTON = ("xpath", "//div[@class='css-nb383z']/*[local-name()='svg']")
    INPUT_IMAGE_URL_EDIT_ITEM_FIELD = ("xpath", "//input[@name = 'imageUrl']")
    INPUT_NAME_EDIT_ITEM_FIELD = ("xpath", "//input[@name = 'name']")
    INPUT_PRICE_EDIT_ITEM_FIELD = ("xpath", "//input[@name = 'price']")
    INPUT_DESCRIPTION_EDIT_ITEM_FIELD = ("xpath", "//textarea[@name = 'description']")
    ITEM_CARD_PICTURE = ("xpath", "//img[@alt='product image']")
    ITEM_CARD_NAME = ("xpath", "//h2[contains(@class,'chakra-heading')]")
    ITEM_CARD_PRICE = ("xpath", "(//p[contains(@class,'chakra-text')])[1]")
    ITEM_CARD_DESCRIPTION = ("xpath", "(//p[contains(@class,'chakra-text')])[2]")
    NEXT_PAGE_BUTTON = ("xpath", "//button[text() = 'Следующая']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)

    def open(self):
        self.driver.get('http://tech-avito-intern.jumpingcrab.com/advertisements/')

    
    def item_data(self):
        name_item = self.fake.word()
        price_item = self.fake.random_int(min=100, max=10000)
        description_item = self.fake.word()
        link_picture_item = self.fake.image_url()
        return {
            "name": name_item,
            "price": price_item,
            "description": description_item,
            "picture_item": link_picture_item
        }

    def create_item(self):
        item_data = self.item_data()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.NAME_ITEM_FIELD)).send_keys(item_data['name'])
        self.wait.until(EC.element_to_be_clickable(self.PRICE_ITEM_FIELD)).send_keys(item_data['price'])
        self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_ITEM_FIELD)).send_keys(item_data['description'])
        self.wait.until(EC.element_to_be_clickable(self.LINK_PICTURE_ITEM_FIELD)).send_keys(item_data['picture_item'])
        self.wait.until(EC.element_to_be_clickable(self.SAVE_ITEM_BUTTON)).click()
        return item_data

    def check_create_item_form(self):
        self.wait.until(EC.invisibility_of_element(self.CREATING_ITEM_FORM))

    def find_items_information(self):
        items = []
        items_picture = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PICTURE))
        items_name = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAME))
        items_price = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICE))
        for picture, name, price in zip(items_picture, items_name, items_price):
            items.append({
            "picture": picture.get_attribute("src"),
            "name": name.text,
            "price": price.text.replace(" ", "").replace("₽", "")
        })
        return items
    
    def open_any_item(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.ITEM_CARD))
        random_index = random.randint(0, len(items)-1)
        items[random_index].click()

    def click_edit_item_button(self):
        button = self.wait.until(EC.presence_of_element_located(self.EDIT_ITEM_BUTTON))
        button.click()

    def input_new_image_url(self):
        image_url = self.fake.image_url()
        url = self.wait.until(EC.element_to_be_clickable(self.INPUT_IMAGE_URL_EDIT_ITEM_FIELD))
        url.clear()
        url.send_keys(image_url)
        return image_url

    def input_new_name(self):
        name = self.fake.word()
        name_field = self.wait.until(EC.element_to_be_clickable(self.INPUT_NAME_EDIT_ITEM_FIELD))
        name_field.clear()
        name_field.send_keys(name)
        return name

    def input_new_price(self):
        price = self.fake.random_int(min=100, max=10000)
        price_field = self.wait.until(EC.element_to_be_clickable(self.INPUT_PRICE_EDIT_ITEM_FIELD))
        price_field.clear()
        price_field.send_keys(price)
        return price
    
    def input_new_description(self):
        description = self.fake.word()
        description_field = self.wait.until(EC.element_to_be_clickable(self.INPUT_DESCRIPTION_EDIT_ITEM_FIELD))
        description_field.clear()
        description_field.send_keys(description)
        return description
    
    def save_item_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_ITEM_BUTTON)).click()
    
    def get_item_card_information(self):
        picture = self.wait.until(EC.presence_of_element_located(self.ITEM_CARD_PICTURE))
        name = self.wait.until(EC.presence_of_element_located(self.ITEM_CARD_NAME))
        price = self.wait.until(EC.presence_of_element_located(self.ITEM_CARD_PRICE))
        description = self.wait.until(EC.presence_of_element_located(self.ITEM_CARD_DESCRIPTION))
        print(description.text)
        return { 
            "picture": picture.get_attribute("src"),
            "name": name.text,
            "price": price.text.replace(" ", "").replace("₽", ""),
            "description": description.text
        }
    
    def find_item(self, name_item):
        self.wait.until(EC.element_to_be_clickable(self.FIND_FIELD)).send_keys(name_item)
        
    def click_find_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FIND_BUTTON)).click()
    
    def check_next_page_button_state(self):
        button = self.wait.until(EC.element_attribute_to_include(self.NEXT_PAGE_BUTTON, "disabled"))




    

    
        
