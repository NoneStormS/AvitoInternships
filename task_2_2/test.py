import pytest
import time
from task_2_2.base_page import BasePage

class TestMainPage:

    def setup_method(self, driver):
        self.main_page = BasePage(self.driver)
        self.main_page.open()

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_create_item(self):
        self.main_page.open()
        created_item = self.main_page.create_item()
        self.main_page.check_create_item_form()
        self.main_page.find_item(created_item['name'])
        self.main_page.click_find_button()
        self.main_page.check_next_page_button_state()
        items = self.main_page.find_items_information()
        pytest.assume(any(item['picture'] == created_item['picture_item'] for item in items))
        pytest.assume(any(item['name'] == created_item['name'] for item in items))
        pytest.assume(any(item['price'] == str(created_item['price']) for item in items))
    
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_edit_item(self):
        self.main_page.open()
        self.main_page.open_any_item()
        self.main_page.click_edit_item_button()
        image_url = self.main_page.input_new_image_url()
        name = self.main_page.input_new_name()
        price = self.main_page.input_new_price()
        description = self.main_page.input_new_description()
        self.main_page.save_item_changes()
        self.driver.refresh()
        item_card_information = self.main_page.get_item_card_information()
        pytest.assume(item_card_information['picture'] == image_url)
        pytest.assume(item_card_information['name'] == name)
        pytest.assume(item_card_information['price'] == str(price))
        pytest.assume(item_card_information['description'] == description)

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_find_item(self):
        self.main_page.open()
        items = self.main_page.find_items_information()
        name_item = items[0]['name']
        self.main_page.find_item(name_item)
        self.main_page.click_find_button()
        self.main_page.check_next_page_button_state()
        found_item = self.main_page.find_items_information()
        for i in found_item:
            assert name_item.lower() in i['name'].lower()

