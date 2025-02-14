import random
import pytest
from task_2_1.api import Api
from task_2_1.model.get_item import GetItem


class TestItem:

    api = Api()

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_create_item(self, session):
        body = self.api.generate_item_body()
        response = self.api.create_item(session, body)
        assert response.status_code == 200
        assert 'Сохранили объявление' in response.json()['status'] 

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_item(self, session):
        body = self.api.generate_item_body()
        create_item = self.api.create_item(session, body)
        assert create_item.status_code == 200
        item_id = create_item.json()['status'].split('Сохранили объявление - ')[1]
        get_item = self.api.get_item(session, item_id)
        assert get_item.status_code == 200
        item = GetItem(**get_item.json()[0])
        pytest.assume(item.id == item_id)
        pytest.assume(item.sellerId == body['sellerID'])
        pytest.assume(item.name == body['name'])
        pytest.assume(item.price == body['price'])
        pytest.assume(item.statistics.contacts == body['statistics']['contacts'])
        pytest.assume(item.statistics.likes == body['statistics']['likes'])
        pytest.assume(item.statistics.viewCount == body['statistics']['viewCount'])

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_statistic(self, session):
        body = self.api.generate_item_body()
        create_item = self.api.create_item(session, body)
        assert create_item.status_code == 200
        item_id = create_item.json()['status'].split('Сохранили объявление - ')[1]
        get_statistic = self.api.get_statistic(session, item_id)
        assert get_statistic.status_code == 200
        pytest.assume(body['statistics']['contacts'] == get_statistic.json()[0]['contacts'])
        pytest.assume(body['statistics']['likes'] == get_statistic.json()[0]['likes'])
        pytest.assume(body['statistics']['viewCount'] == get_statistic.json()[0]['viewCount'])


    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_all_seller_items(self, session):
        body = self.api.generate_item_body()
        create_item = self.api.create_item(session, body)
        item_id = create_item.json()['status'].split('Сохранили объявление - ')[1]
        assert create_item.status_code == 200
        seller_item = self.api.get_seller_items(session, body['sellerID'])
        assert seller_item.status_code == 200
        seller = GetItem(**seller_item.json()[0])
        pytest.assume(body['sellerID'] == seller.sellerId)
        pytest.assume(item_id== seller.id)
        pytest.assume(body['name'] == seller.name)
        pytest.assume(body['price'] == seller.price)
        pytest.assume(body['statistics']['contacts'] == seller.statistics.contacts)
        pytest.assume(body['statistics']['likes'] == seller.statistics.likes)
        pytest.assume(body['statistics']['viewCount'] == seller.statistics.viewCount)


    @pytest.mark.negative
    @pytest.mark.regression
    def test_get_item_with_invalid_id(self, session):
        response = self.api.get_item(session, -1)
        assert response.status_code == 400
        assert response.json()['result']['message'] == 'передан некорректный идентификатор объявления'

    @pytest.mark.negative
    @pytest.mark.regression
    def test_get_invalid_seller_item(self, session):
        response = self.api.get_seller_items(session, -100000)
        assert response.status_code == 200
        assert len(response.json()) == 0

    @pytest.mark.parametrize("value",[
        pytest.param("test", id="string"),
        pytest.param("", id="empty string"),
        pytest.param(None, id="None")
        ])
    @pytest.mark.negative
    @pytest.mark.regression
    def test_create_item_validate_seller_id(self, session, value):
        body = {
            "sellerID": value,
            "name": "test",
            "price": 1,
            "statistics": {
                "contacts": 1,
                "likes": 1,
                "viewCount": 1
                }
            }
        if value is None:
            body.pop("sellerID")
        create_item = self.api.create_item(session, body)
        assert create_item.status_code == 400
        assert create_item.json()['status'] == 'не передано тело объявлени'

    @pytest.mark.parametrize("value",[
        pytest.param(123, id="integer"),
        pytest.param("", id="empty string"),
        pytest.param(None, id="None")
        ])
    @pytest.mark.negative
    @pytest.mark.regression
    def test_create_item_validate_name(self, session, value):
        body = {
            "sellerID": random.randint(111111, 999999),
            "name": value,
            "price": 1,
            "statistics": {
                "contacts": 1,
                "likes": 1,
                "viewCount": 1
                }
            }
        if value is None:
            body.pop("name")
        create_item = self.api.create_item(session, body)
        assert create_item.status_code == 400
        assert create_item.json()['status'] == 'не передано тело объявлени'

    @pytest.mark.parametrize("value",[
        pytest.param("test", id="string"),
        pytest.param("", id="empty string"),
        pytest.param(None, id="None")
        ])
    @pytest.mark.negative
    @pytest.mark.regression
    def test_create_item_validate_price(self, session, value):
        body = {
            "sellerID": random.randint(111111, 999999),
            "name": self.api.fake.name(),
            "price": value,
            "statistics": {
                "contacts": 1,
                "likes": 1,
                "viewCount": 1
                }
            }
        if value is None:
            body.pop("price")
        create_item = self.api.create_item(session, body)
        assert create_item.status_code == 400
        assert create_item.json()['status'] == 'не передано тело объявлени'

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_create_item_without_statistics(self, session):
        body = self.api.generate_item_body(include_statistics=False)
        create_item = self.api.create_item(session, body)
        assert create_item.status_code == 200
        assert 'Сохранили объявление' in create_item.json()['status']
        item_id = create_item.json()['status'].split('Сохранили объявление - ')[1]
        get_item = self.api.get_item(session, item_id)
        assert get_item.status_code == 200
        item = GetItem(**get_item.json()[0])
        assert item.statistics.contacts == 0
        assert item.statistics.likes == 0
        assert item.statistics.viewCount == 0