import pandas as pd
import numpy as np

import xlrd,os
all_datas = pd.Series()
for i in os.listdir('./excels'):
    xls = xlrd.open_workbook("./excels/"+str(i) , on_demand=True)
    for j in xls.sheet_names():
        file = pd.read_excel("./excels/"+str(i) , j)
        file = pd.DataFrame(data= file).T
        file = file.iloc[1:,]
        file.columns = ['date' , 'market cap' , 'return']
        file['name'] = j
        for t in range(1,3):
            file[t] = np.NaN
            for u in range(t,len(file)):
               file[t].iloc[u] = file["return"].iloc[u-t]
        for t in range(24,37,12):
            file[t] = np.NaN
            for u in range(t,len(file)):
               file[t].iloc[u] = file["return"].iloc[u-t]
        break
    break

# print(file[11])
print(file[24])
print(file[36])
print(file)