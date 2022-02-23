import pandas as pd
import numpy as np


class DemandForecastData:
    url = None
    raw_data = None

    def __init__(self, page):
        self.url = f"http://www.38.co.kr/html/fund/index.htm?o=r&page={page}"
        self.raw_data = pd.read_html(self.url, match='종목명')
        self.__drop_unused_columns()

    def __drop_unused_columns(self):
        self.raw_data = self.raw_data[0].drop(columns=['Unnamed: 6', 'Unnamed: 7']).dropna()
        self.raw_data = self.raw_data.replace('-', np.nan)
        self.raw_data = self.raw_data.set_index('종목명')

    def __cleaning_demand_forecast_time(self):
        """
        2022.01.01~01.24 이렇게 되어 있는 데이터를 각각 2022.01.01 | 2022.01.24 이렇게 클리닝
        :return: pd.DataFrame
        """
        demant_forecast_time = self.raw_data[['수요예측일']]
        demant_forecast_time['수요예측일'].str.split('.')
        demant_forecast_time['year'] = list(map(lambda x: x[0], demant_forecast_time['수요예측일'].str.split('.')))
        demant_forecast_time['demand_forecast_start'] = list(
            map(lambda x: x[0], demant_forecast_time['수요예측일'].str.split('~')))
        demant_forecast_time['demand_forecast_end'] = list(
            map(lambda x: x[1], demant_forecast_time['수요예측일'].str.split('~')))
        demant_forecast_time['demand_forecast_end'] = demant_forecast_time['year'] + '.' + demant_forecast_time[
            'demand_forecast_end']
        return demant_forecast_time[['demand_forecast_start', 'demand_forecast_end']]

    def __cleaning_hope_price(self):
        pass
        # hope_price = self.raw_data['희망공모가(원)'].str.split('~')
        # return (pd.DataFrame(
        #     list(
        #         map(
        #             lambda x: [float(x[0].replace(',', ''))
        #                 , float(x[1].replace(',', ''))
        #                        ], hope_price)), columns=['hope_price_min', 'hope_price_max'], index=ipo_df.index)