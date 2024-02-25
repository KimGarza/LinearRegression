import pandas as pd

def load_CSV():
    data = pd.read_csv('./ice_cream_sales_temps.csv')
    print(data.head()) # prints 1st 5 rows
