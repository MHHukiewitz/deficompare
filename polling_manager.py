import data_sources as ds


class PollingManager:
    def __init__(self, db):
        self.db = db

        self.solana_metrics = ds.SolanaMetricProvider()  # constructor automatically polls data
        self.etherium_metrics = ds.EthereumMetricProvider()
        self.serum_metrics = ds.SerumMetricProvider()
        self.uniswap_metrics = ds.UniswapMetricProvider()

        print(self.solana_metrics)
        print(self.etherium_metrics)
        print(self.serum_metrics)
        print(self.uniswap_metrics)

    def poll(self):
        solana_data = self.solana_metrics.poll()
        self.solana_metrics.store_row_in_db(self.db, self.solana_metrics.name, solana_data)

        etherium_data = self.etherium_metrics.poll()
        self.etherium_metrics.store_row_in_db(self.db, ETHERIUM_TOKEN_CODE, etherium_data)

        serum_data = self.serum_metrics.poll()
        self.serum_metrics.store_row_in_db(self.db, SERUM_EXCHANGE_CODE, serum_data)

        uniswap_data = self.uniswap_metrics.poll()
        self.uniswap_metrics.store_row_in_db(self.db, UNISWAP_EXCHANGE_CODE, uniswap_data)




