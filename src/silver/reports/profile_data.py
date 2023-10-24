from sqlalchemy import text as sql_text, create_engine
from ydata_profiling import ProfileReport
import pandas as pd
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus as urlquote

load_dotenv()

class ProfileData:

    def __init__(self):
        self.__postgres_user = os.getenv("POSTGRES_USER")
        self.__postgres_password = os.getenv("POSTGRES_PASSWORD")

        self.__conn_string = f"postgresql://{self.__postgres_user}:{urlquote(self.__postgres_password)}@localhost:5432/Analytics_Engineering"
        self.engine = create_engine(self.__conn_string)

    @staticmethod
    def report_profile(df, title) -> str:

        profile = ProfileReport(
            df, title="Pandas Profiling Report")

        profile.to_file(f"{title}.html")
        return "Sucesso"

    @staticmethod
    def query_table(params: str) -> str:
        return f"""
              SELECT * 
              FROM public."{params}";
            """


df_reviews_silver = pd.read_sql(sql=sql_text(
    ProfileData().query_table("Reviews_Silver")), con=ProfileData().engine.connect())

ProfileData().report_profile(df_reviews_silver, 'reviews_silver')