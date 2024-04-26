import time

from fastapi import FastAPI
from asyncio import sleep

import random

max_value = 100
hit_per_of_slow_latency = max_value * 0.01  # 1%

app = FastAPI()


@app.post("/hello")
async def hello_world():
    start = time.perf_counter()
    if random.random() <= 0.01:
        await sleep(random.uniform(0.01, 0.1))  # 100ms ~ 10m
    end = time.perf_counter()

    latency = (end - start) * 1000  # ms
    return {"latency": latency}
