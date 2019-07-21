# coding:utf-8
#数据变换
from sklearn import preprocessing
import numpy as np
#初始化数据
min = 5000.
max = 58000.
income = 16000.
x = np.array([[min], [max], [income]])
#将数据[0 1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print((minmax_x))
print((minmax_x)[2])
