import pandas as pd


class MetricsService:
    def __init__(self, db):
        self.db = db

    def get_df_by_token(self, token_code='') -> pd.DataFrame:
        return self.db.get_token_df(token_code)

    def get_dummy_data_eth(self, token_code='eth') -> pd.DataFrame:
        # Note: datetime is just python datetime.datetime.now()
        df = pd.DataFrame(
            [
                ['2021-02-24 21:20:00.000000', 1693.78, 110.0,   96.0,  3.9435454543623435, 12.804878048780488],
                ['2021-02-24 21:21:00.000000', 1507.78, 100.0,   60.0,  2.3435454353453243, 12.404761904761905],
                ['2021-02-24 21:22:00.000000', 1796.78, 140.0,   100.0, 4.1435454353453242, 13],
                ['2021-02-24 21:23:00.000000', 1592.78, 120.0,   93.0,  3.9435453454356346, 12.047619047619047],
                ['2021-02-24 21:24:00.000000', 1990.78, 110.0,   97.0,  3.9126317999999998, 12.047619047619047],
            ],
            columns=['datetime', 'current_coin_price', 'avg_gas_price', 'avg_tx_time', 'avg_tx_price', 'last_block_time']
        )
        return df

    def get_dummy_data_sol(self, token_code='eth') -> pd.DataFrame:
        # Note: datetime is just python datetime.datetime.now()
        df = pd.DataFrame(
            [
                ['2021-02-24 21:20:00.000000', 16.17, .000000001,   5020,  0.00008, None],
                ['2021-02-24 21:21:00.000000', 17.14, .000000001,   5020,  0.00008, None],
                ['2021-02-24 21:22:00.000000', 18.16, .000000001,   5020, 0.00008, None],
                ['2021-02-24 21:23:00.000000', 13.13, .000000001,   5020,  0.00008, None],
                ['2021-02-24 21:24:00.000000', 19.1, .000000001,   5020,  0.00008, None],
            ],
            columns=['datetime', 'current_coin_price', 'avg_gas_price', 'avg_tx_time', 'avg_tx_price', 'last_block_time']
        )
        return df

