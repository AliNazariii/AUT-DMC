import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
print(df.describe())
edited_df = np.array(df.values)
to_delete = []
for index, row in df.iterrows():
    if math.isnan(row['Price']) or math.isnan(row['FROM']) or math.isnan(row['TO']) or math.isnan(
            row['Departure_Time']):
        print(row)
        # print(index)
        to_delete.append(index)

print(len(to_delete))
print(to_delete)
df.drop(to_delete)

df.to_csv('cleaned.csv', index=False)
