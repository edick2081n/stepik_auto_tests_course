import time
from locust import HttpUser, task, between
from locust_plugins.users.webdriver import WebdriverUser
from lesson_4.test_lesson4_3_step2 import test_guest_can_add_product_to_basket

class User(WebdriverUser):
    wait_time = between(1, 5)



    @task
    def hello_world(self):
        with self.request(name='hello_world') as request:
            test_guest_can_add_product_to_basket(request.client)
