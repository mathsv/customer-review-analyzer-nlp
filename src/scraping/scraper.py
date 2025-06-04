"""
    A scraper for Google Play product reviews using SerpAPI.
"""

from datetime import datetime
import os
import serpapi
import pandas
from dotenv import load_dotenv

class Scraper:
    """
        A scraper for Google Play product reviews using SerpAPI.
    """
    def __init__(self):
        load_dotenv('../.env')

        self.SERPAPI_KEY:str = os.getenv('SERPAPI_KEY')
        self.PRODUCT_ID:str = os.getenv('PRODUCT_ID')

        self.dfs:list = []
        self.client = serpapi.Client(api_key=self.SERPAPI_KEY)

        self.scrap_data()
        self.save_data_to_file()

    def scrap_data(self):
        """
            Scrap data from Google Play.
        """
        for i in range(10700):  #Get 214K reviews
            results = self.client.search(
                engine='google_play_product',
                product_id=self.PRODUCT_ID,
                store='apps',
                all_rewiews=True,
                num=199,
                platform='phone',
                gl='br',
                hl='pt-br',
                next_page_token=results['serpapi_pagination']['next']
            )

            self.dfs.append(
                pandas.DataFrame(
                    results['reviews']
                )
            )

    def save_data_to_file(self):
        """
            Save the data to a file.
        """
        date = str(datetime.now().day).zfill(2) + '_' + str(datetime.now().month).zfill(2) + '_' + str(datetime.now().year)

        data = pandas.concat(self.dfs)
        data.to_parquet(f'../data/raw/{self.PRODUCT_ID}_{date}.parquet')
