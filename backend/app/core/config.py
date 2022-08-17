import os

PROJECT_NAME = os.getenv("PROJECT_NAME")

user_name = os.getenv("BACKEND_USERNAME")
password = os.getenv("BACKEND_PASSWORD")
host = "db"
database_name = os.getenv("BACKEND_DATABASE")

DATABASE_URI = f"mysql://{user_name}:{password}@{host}/{database_name}?charset=utf8"


API_STR = "/api/v1"
MAP_URL = lambda route: f"{API_STR}/{route}"