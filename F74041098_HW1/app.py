import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

raw_data=pd.read_csv("data.csv", usecols=lambda x: x.upper() in ['尖峰負載(MW)'])
data=raw_data.values
data=data.transpose().ravel()
train_day=546 #2018/6/30
train_data=data[:train_day]

model = ExponentialSmoothing(train_data,seasonal_periods=185,seasonal='add').fit(use_boxcox=True)
pred = model.predict(len(data)+1,len(data)+7)

csv = open("submission.csv", "w") 
columnTitleRow = "date,peak_load(MW)\n"
csv.write(columnTitleRow)
pred_date=['20190402','20190403','20190404','20190405','20190406','20190407','20190408']
for i in range(7):
	row = pred_date[i] + "," + str(pred[i]) + "\n"
	csv.write(row)

