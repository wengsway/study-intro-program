#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 4:38 PM 
# File  : compare_highs_lows.py 
# IDE   : PyCharm

# 16-2
# Can not download weather data of San Francisco, so pass 16-1
# pass 16-3 and 16-4 for the same reason.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期和最高温
filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'

with open(filename_1) as f_1:
    reader_1 = csv.reader(f_1)
    f_1_header_row = next(reader_1)

    dates_1, highs_1, lows_1 = [], [], []
    for row in reader_1:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_1.append(current_date)
            highs_1.append(high)
            lows_1.append(low)

with open(filename_2) as f_2:
    reader_2 = csv.reader(f_2)
    f_2_header_row = next(reader_2)

    dates_2, highs_2, lows_2 = [], [], []
    for row in reader_2:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_2.append(current_date)
            highs_2.append(high)
            lows_2.append(low)


# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c='red', alpha=0.8, label='death_valley_high')
plt.plot(dates_1, lows_1, c='blue', alpha=0.8, label='death_valley_low')
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.plot(dates_2, highs_2, c='red', alpha=0.5, label='sitka_high')
plt.plot(dates_2, lows_2, c='blue', alpha=0.5, label='sitka_low')
plt.legend(loc='best')

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\n Death Valley and sitka", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()