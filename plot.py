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

flight_count = np.zeros((20, 76, 76, 731))

# find the number of flight in each day and in each airline
for index, row in df.iterrows():
    log_date = int(row['Log_Date'][8:10])
    if row['Log_Date'][2:4] == '96':
        log_date += 366
    if int(row['Log_Date'][5:7]) > 6:
        log_date += 186
        log_date += (int(row['Log_Date'][5:7]) - 7) * 30
    else:
        log_date += (int(row['Log_Date'][5:7]) - 1) * 31

    flight_count[int(row['AL']) - 1][int(row['FROM']) - 1][int(row['TO']) - 1][log_date - 1] += 1
    print(index)

days = range(731)
plt.plot(days, flight_count[1][48][66][0:])
plt.show()

#   ## draw 76*76 subplots like a matrix
# fig, ax = plt.subplots(nrows=76, ncols=76)
# for i in range(76):
#     print(i)
#     for j in range(76):
#         if i == j:
#             plt.subplot(76, 76, (i * 76) + (j + 1))
#             plt.plot(0, 0)
#         else:
#             for k in range(20):
#                 plt.subplot(76, 76, (i * 76) + (j + 1))
#                 # plt.plot(days, flight_count[k][i][j][0:])
#
# plt.show()

#   ##    subplot test    ##
# fig, ax = plt.subplots(nrows=8, ncols=8)
#
# x = range(10)
# y = range(10)
#
# plt.subplot(8, 8, 1)
# plt.plot(x, y)
#
# plt.subplot(8, 8, 2)
# plt.plot(x, y)
#
# plt.subplot(8, 8, 3)
# plt.plot(x, y)
#
# plt.subplot(8, 8, 7)
# plt.plot(x, y)
#
# plt.show()
