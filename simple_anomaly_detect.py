import pandas
import sys

path = "opsview-graph-data.csv"
metric_name = 'opsviewCPU'
date_column = "time"

try:
    path = sys.argv[1]
except IndexError:
    path = "opsview-graph-data.csv"
    
df = pandas.read_csv(path, header=0, quotechar='"', error_bad_lines=False, parse_dates=[date_column]).sort_values(by=date_column)

std = df[metric_name].std()

recentdf = df[metric_name][-3:]
print(df)
recentMean = recentdf.mean()

rolling_average_period_df = df[metric_name][-30:]
recent_rolling_period = rolling_average_period_df.mean()

print("Standard dev: {}, Rolling Mean: {}, Current Value: {}".format(std, recent_rolling_period, recentMean))

if abs(recent_rolling_period - recentMean) > std:
    print("we have an anomaly")
