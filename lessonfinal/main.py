import csv
import pandas as pd

def getStockNames() -> pd.Series:
    with open('codeSearch.csv',encoding='utf-8',newline='') as file:
        next(file)
        csv_reader = csv.reader(file)
        stock_codes = {}
        for item in csv_reader:
            key  =  item[2]
            stock_codes[key] = item[3]
        
    code_series:pd.Series = pd.Series(stock_codes)
    return code_series

stockNames:pd.Series = getStockNames()
print(stockNames)