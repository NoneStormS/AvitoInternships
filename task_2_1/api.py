import requests
from faker import Faker
import random
from task_2_1.endpoints import EndPoints
from task_2_1.headers import Headers

class Api:

    fake = Faker()

    def generate_item_body(self, include_statistics=True):
        item_body = {
            "sellerID": random.randint(111111, 999999),
            "name": self.fake.name(),
            "price": random.randint(10, 100),
        }
        if include_statistics:
            item_body["statistics"] = {
                "contacts": random.randint(1, 10),
                "likes": random.randint(1, 20),
                "viewCount": random.randint(1, 5)
            }
        return item_body


    def create_item(self, session: requests.Session, item_data: dict):
        response = session.post(url=f"{session.base_url}{EndPoints.CREATE_ITEM}",
                                headers=Headers.CREATE_ITEM_HEADERS,
                                json=item_data)
        return response
    
    def get_item(self, session: requests.Session, listing_id: str):
        response = session.get(url=f"{session.base_url}{EndPoints.GET_ITEM(listing_id)}", 
                              headers=Headers.GET_ITEMS_HEADERS)
        return response
    
    def get_statistic(self, session: requests.Session, listing_id: int):
        response = session.get(url=f"{session.base_url}{EndPoints.GET_STATISTIC(listing_id)}", 
                              headers=Headers.GET_ITEMS_HEADERS)
        return response
    
    def get_seller_items(self, session: requests.Session, seller_id: int):
        response = session.get(url=f"{session.base_url}{EndPoints.GET_SELLER_ITEM(seller_id)}", 
                              headers=Headers.GET_ITEMS_HEADERS)
        return response
    