# coding:utf-8
# 小数定标
from sklearn import preprocessing
import numpy as np

# 初始化数据
x = np.array([[0., -3., 1.],
              [3., 1.,  2.],
              [0., 1., -1.]])

# 将数据进行小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print scaled_x
