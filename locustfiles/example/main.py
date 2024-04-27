# -*- coding: utf-8 -*-
from locust import task, HttpUser, between


class SampleAPIServerUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(0.1, 0.5)

    @task
    def post_hello(self):
        self.client.post("/hello", data={"foo": "bar"})

# Debug Mode
# if __name__ == "__main__":
#     from locust import run_single_user
#
#     run_single_user(SampleAPIServerUser)
