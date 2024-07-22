import asyncio
import datetime

import aiofiles
import httpx
from fastapi import FastAPI

app = FastAPI()


async def heavy_task(task_id: str):
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            client.post(f"http://localhost:8000/first_job?task_id={task_id}"),
            client.post(f"http://localhost:8000/second_job?task_id={task_id}"),
        )
        await client.post(f"http://localhost:8000/third_job?task_id={task_id}")


@app.post("/first_job")
async def first_job(task_id: str):
    await asyncio.sleep(3)
    async with aiofiles.open("app.log", mode="a") as log_file:
        msg = f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Done first job of {task_id}\n"
        await log_file.write(msg)


@app.post("/second_job")
async def second_job(task_id: str):
    await asyncio.sleep(3)
    async with aiofiles.open("app.log", mode="a") as log_file:
        msg = f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Done second job of {task_id}\n"
        await log_file.write(msg)


@app.post("/third_job")
async def third_job(task_id: str):
    await asyncio.sleep(3)
    async with aiofiles.open("app.log", mode="a") as log_file:
        msg = f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Done third job of {task_id}\n"
        await log_file.write(msg)


@app.post("/")
async def add_task(task_id: str):
    async with aiofiles.open("app.log", mode="a") as log_file:
        msg = f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} task {task_id} is scheduled\n"
        await log_file.write(msg)
    asyncio.create_task(heavy_task(task_id))
    return {"message": "tasks are set"}
