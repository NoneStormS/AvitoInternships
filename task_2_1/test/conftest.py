import pytest
import requests

@pytest.fixture(scope="function")
def session():
    base_url = "https://qa-internship.avito.com"
    client = requests.Session()
    client.base_url = base_url  
    yield client
    client.close()

    


