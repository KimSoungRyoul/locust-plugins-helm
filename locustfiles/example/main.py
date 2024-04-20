# -*- coding: utf-8 -*-
from locust import FastHttpUser, task, between
from locust_plugins.connection_pools import FastHttpPool

from lib.example_functions import choose_random_page

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


class WebsiteUser(FastHttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.pool = FastHttpPool(user=self)

    @task
    def get_index(self):
        self.pool.get("/", headers=default_headers)

    @task(3)
    def get_random_page(self):
        self.pool.get(choose_random_page(), headers=default_headers)
