import pandas as pd
import numpy as np


class DemandForecastData:
    __url = None
    __raw_data = None
    __cleaning_data = None

    def __init__(self, page):
        self.__url = f"http://www.38.co.kr/html/fund/index.htm?o=r&page={page}"
        self.__raw_data = pd.read_html(self.__url, match='종목명')
        self.__drop_unused_columns()
        demand_forecast_time = self.__get_demand_forecast_time()
        hope_time = self.__get_hope_price()
        raw_data_en = self.__change_kr_to_en_columns()
        self.__cleaning_data = pd.concat([raw_data_en, demand_forecast_time, hope_time], axis=1)
        self.__cleaning_data.index.name = 'name'

    def get(self):
        return self.__cleaning_data

    def __drop_unused_columns(self):
        self.__raw_data = self.__raw_data[0].drop(columns=['Unnamed: 6', 'Unnamed: 7']).dropna()
        self.__raw_data = self.__raw_data.replace('-', np.nan)
        self.__raw_data = self.__raw_data.set_index('종목명')

    def __get_demand_forecast_time(self) -> pd.DataFrame:
        """
        2022.01.01~01.24 이렇게 되어 있는 데이터를 각각 2022.01.01 | 2022.01.24 이렇게 클리닝
        :return: pd.DataFrame
        """
        demant_forecast_time = self.__raw_data[['수요예측일']]
        demant_forecast_time['수요예측일'].str.split('.')
        demant_forecast_time['year'] = list(map(lambda x: x[0], demant_forecast_time['수요예측일'].str.split('.')))
        demant_forecast_time['demand_forecast_start'] = list(
            map(lambda x: x[0], demant_forecast_time['수요예측일'].str.split('~')))
        demant_forecast_time['demand_forecast_end'] = list(
            map(lambda x: x[1], demant_forecast_time['수요예측일'].str.split('~')))
        demant_forecast_time['demand_forecast_end'] = demant_forecast_time['year'] + '.' + demant_forecast_time[
            'demand_forecast_end']
        return demant_forecast_time[['demand_forecast_start', 'demand_forecast_end']]

    def __get_hope_price(self) -> pd.DataFrame:
        """
        희망공모가를 나눠준다 16000~17000이면 16000|17000 이렇게 나눠준다.
        :return:
        """
        hope_price = self.__raw_data['희망공모가(원)'].str.split('~')
        return (pd.DataFrame(
            list(
                map(
                    lambda x: [float(x[0].replace(',', ''))
                        , float(x[1].replace(',', ''))
                               ], hope_price)), columns=['hope_price_min', 'hope_price_max'],
            index=self.__raw_data.index)
        )

    def __change_kr_to_en_columns(self) -> pd.DataFrame:
        return (self.__raw_data
                .reset_index()[['종목명', '확정공모가', '공모금액(백만)', '주간사']]
                .rename(columns={'종목명': 'stock', '확정공모가': 'ipo_price', '공모금액(백만)': 'ipo_value', '주간사': 'security'})
                .set_index('stock')
                )
