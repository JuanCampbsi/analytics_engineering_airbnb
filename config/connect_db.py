import os
from dotenv import load_dotenv
from urllib.parse import quote_plus as urlquote
from sqlalchemy import create_engine

load_dotenv()


class ConnectDataBase:

    def __init__(self):
        self.__postgres_user = os.getenv("POSTGRES_USER")
        self.__postgres_password = os.getenv("POSTGRES_PASSWORD")

        self.__conn_string = f"postgresql://{self.__postgres_user}:{urlquote(self.__postgres_password)}@localhost:5432/Analytics_Engineering"

    def engine(self):
        return create_engine(self.__conn_string)
