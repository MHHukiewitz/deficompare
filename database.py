#!/usr/bin/python

import sqlite3
import pandas as pd

from constants import TOKEN_CODES

class SQLLiteDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

        print("Opened database successfully")

        # Create a table for each token
        for token_code in TOKEN_CODES:
            self.conn.execute(f'''CREATE TABLE IF NOT EXISTS {token_code}_metrics 
                     (id INT PRIMARY KEY     NOT NULL,
                     timestamp TIMESTAMP CURRENT_TIMESTAMP,
                     tx_fee            DOUBLE     NOT NULL,
                     tx_delay            DOUBLE     NOT NULL
                     );''')

        self.conn.close()

    def get_token_df(self, token_code):
        self.conn = sqlite3.connect('test.db')

        print("Opened database successfully")

        # Create a table for each token
        df = pd.read_sql_query(f"SELECT * from {token_code}_metrics", self.conn)

        self.conn.close()
        return df




