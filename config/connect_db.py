import os
from dotenv import load_dotenv
from urllib.parse import quote_plus as urlquote
from sqlalchemy import create_engine

load_dotenv()


class ConnectDataBase:

    def __init__(self):
        self.__postgres_user = "postgres"
        self.__postgres_password = "root"
        self.__conn_string = f"postgresql://{self.__postgres_user}:{urlquote(self.__postgres_password)}@localhost:5432/Analytics_Engineering"
        self.__conn_string_great_ex = f"postgresql+psycopg2://{self.__postgres_user}:{urlquote(self.__postgres_password)}@localhost:5432/Analytics_Engineering"

    @property
    def conn_string(self) -> str:
        return self.__conn_string

    @property
    def conn_string_great_ex(self) -> str:
        return self.__conn_string_great_ex

    def engine(self):
        return create_engine(self.conn_string)
