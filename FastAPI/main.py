from fastapi import FastAPI
from FastAPI.utils.helper import construct_welcome_message_with_name, calculate_profile_summary
from profiler import profile_function_sync, profile_function_async
import os

app = FastAPI()


@app.get("/")
@profile_function_sync
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
@profile_function_async
async def say_hello(name: str):
    return construct_welcome_message_with_name(name)


# Add an endpoint to retrieve the profiling summary from any random container
@app.get("/profiling_summary")
async def get_profiling_summary():
    return {"Result from worker {}".format(os.getpid()): calculate_profile_summary()}


# Add an endpoint to retrieve the profiling summary given you know number of containers running
@app.get("/profiling_summary/{container_count}")
async def get_profiling_summary(container_count):
    return {
        "Result from worker {}|{}".format(
            os.getpid(), hash(os.getpid()) % int(container_count) + 1
        ): calculate_profile_summary()
    }
