import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Color:
    A = '#ff0000'  # for 1
    B = '#d1490a'  # for 2
    C = '#db8918'  # for 3
    D = '#ccb912'  # for 4
    E = '#a8c918'  # for 5
    F = '#7fdb06'  # for 6
    G = '#2a7210'  # for 7
    H = '#a7e8a2'  # for 8
    I = '#52eacd'  # for 9
    J = '#1c826e'  # for 10
    K = '#04a0f4'  # for 11
    L = '#0e5277'  # for 12
    M = '#002aff'  # for 13
    N = '#4c5db5'  # for 14
    O = '#4c46aa'  # for 15
    P = '#7936c1'  # for 16
    Q = '#2e025e'  # for 17
    R = '#aa09c6'  # for 18
    S = '#c910a4'  # for 19
    T = '#d11f66'  # for 20


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


def find_flight_count(data_frame):
    flight_count = np.zeros((20, 76, 76, 731))
    for index, row in data_frame.iterrows():
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
    np.save('flight_count.npy', flight_count)


# df = pd.read_csv('data.csv')
# df = clean_data(df)

df = pd.read_csv('cleaned.csv')

print(df.head())
# print(df.describe())

# find_flight_count(df)
flight_count = np.load('flight_count.npy')

days = range(731)
color = Color()
for i in range(76):
    print(i)
    for j in range(76):
        if i != j:
            for k in range(20):
                if np.sum(flight_count[k][i][j][0:]) != 0.0:
                    color_ascii = chr(k + 65)
                    plt.plot(days, flight_count[k][i][j][0:], color=getattr(color, color_ascii))
                    plt.xlabel('Days')
                    plt.ylabel('Number of requests')
                    plt.title('Flight from ' + str(i + 1) + ' to ' + str(j + 1))
                    plt.savefig('needed_visualize/' + str(i + 1) + '-' + str(j + 1) + '.png')
            plt.clf()
