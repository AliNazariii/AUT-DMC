import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def clean_data(data_frame):
    to_delete = []
    for index, row in data_frame.iterrows():
        if math.isnan(row['Price']) or math.isnan(row['FROM']) or math.isnan(row['TO']) or math.isnan(
                row['Departure_Time']):
            print(row)
            # print(index)
            to_delete.append(index)

    print(len(to_delete))
    # print(to_delete)
    data_frame = data_frame.drop(to_delete)

    data_frame.to_csv('cleaned.csv', index=False)
    return data_frame


# df = pd.read_csv('data.csv')
# df = clean_data(df)
df = pd.read_csv('cleaned.csv')
print(df.head())
print(df.describe())

flight_count = np.zeros((76, 76, 20))

for index, row in df.iterrows():
    flight_count[int(row['FROM']) - 1][int(row['TO']) - 1][int(row['AL']) - 1] += 1.0
    print(index)

