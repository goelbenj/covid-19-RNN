import numpy as np
import pandas as pd
import tensorflow as tf

data = pd.read_csv("train.csv")
data_size = len(data['Id'])
data = data.query("Date>'2020-01-29' and Date<='2020-03-11'")

for country in data.Country_Region.unique():
    print(country)
    count = 0
    for province in data.query("Country_Region=='"+country+"'").Province_State:
        count+=1

    print(count)
    