# NumPy快速处理数据-学习总结

## 1.使用NumPy让Python的科学计算更加高效
- 区别：为什么不是直接使用list，而是更加高效的NumPy
- 原因：NumPy重新定义了数据结构，使用的是C语言编写
- 规则：避免使用隐式拷贝，而是采用就地操作的方式：如使用x *= 2,不用y = x*2

## NumPy包含的两个重要的对象：ndarray和ufunc
### ndarray（N-dimensional array object ） 对象
- ndarray:多维数组
- 一维数组的秩=1，二维数组的秩=2，三维数组的秩=3
- 线性数组称为一个轴（axes），秩就是描述轴的数量
### 创建数组：
```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1,1]=10 # 直接赋值进行修改
print(a.shape)  # 获取数组的大小
print(b.shape) 
print(a.dtype) # 获取元素的属性
print(b)

# 运行结果
'''
(3,)
(3, 3)
int32
[[ 1  2  3]
 [ 4 10  6]
 [ 7  8  9]]
'''
```
### 结构素组
- 目的：统计一个班级里面的学生的姓名、年龄、以及语文、英语、数学成绩：
- NumPy的实现方式：
```python
import numpy as np
# 使用dtype定义结构类型
persontype = np.dtype({
    # 很明显names和formats是关键字，不能出错！
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
# 定义数组的时候用array中指定了的结构数组类型dtype=persontype
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
# 分别获取所有的年龄，语文，数学，英语的数据
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
# 求得各个属性的平均值mean
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))
'''
# 运行结果
28.25
77.5
93.25
93.75
'''
```
## ufunc运算
- universal function的缩写 
- 计算速度快

### 连续数组的创建
- 可以使用arange或者linspace函数创建
```python
import numpy as np
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
```
- 区别：都会产生列表[1,3,5,7,9],但是使用的方法是不同的，前者使用2作为步长，不包括尾部元素；后者使用等差数列，限定个数，包括尾部元素

### 进行算数运算
- 使用NumPy进行加减乘除和求n次方和求余，例如：
```python
import numpy as np
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
# 产生数组[1,3,5,7,9]
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
# 求余也可以使用np.mod(x1,x2)
print(np.remainder(x1, x2))

# 运算的结果为：
'''
[ 2.  6. 10. 14. 18.]
[0. 0. 0. 0. 0.]
[ 1.  9. 25. 49. 81.]
[1. 1. 1. 1. 1.]
[1.00000000e+00 2.70000000e+01 3.12500000e+03 8.23543000e+05
 3.87420489e+08]
[0. 0. 0. 0. 0.]
'''
```
### 统计函数
- 统计学里面的值进行计算：最大最小值、平均值、是否符合正态分布、方差、标准差
#### 计数组/ 矩阵中的最大函数amax(),最小函数amin()
- 示例代码：
```python
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.amin(a)) # 求得（计数组）矩阵的最小元素
print(np.amin(a,0)) # axis=0 就是按照行获取
print(np.amin(a,1)) # axis=1 就是按照列获取 
print(np.amax(a)) #获取最大值
print(np.amax(a,0)) # 按照行获取最大
print(np.amax(a,1)) # 按照列获取最大

'''
# 运行结果：
1
[1 2 3]
[1 4 7]
9
[7 8 9]
[3 6 9]
'''
```
#### 统计最大值和最小值之差
```python
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.ptp(a))  # 数值中最大最小值之差
print(np.ptp(a,0)) # 每行中最大最小值之差6
print(np.ptp(a,1)) # 每列中最大最小值之差2
'''
# 运行结果
8
[6 6 6]
[2 2 2]
'''
```
#### 统计数组的百分位数percentile()
##### 引入：
学习Python的NumPy科学计算类库的时候遇到计算百分位数，使用NumPy实现的代码很简单，直接调用就行，如下所示：
```python
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# 50是P（0～100），表示第p百分位数
print(np.percentile(a, 50))
# 结果：5.0
print(np.percentile(a, 50, axis=0))
# 跨行（axis=0）结果：[4. 5. 6.]
print(np.percentile(a, 50, axis=1))
# 跨列（axis=1）结果：[2. 5. 8.]
print(np.percentile(a,30))
# 结果：3.4
```
##### 疑问
最后的计算30的百分位数3.4是怎样得到的呢？就想了解一下计算原理，百度一下后，总结下个人理解
##### 原理
计算公式：①(n−1)∗p=i+j；②result = (1−j)∗arr[i]+j∗arr[i+1]
n：数组的个数：1, 2, 3, 4, 5, 6, 7, 8, 9 ，总共9个，n=9;
p: 需要计算的百分位数，这里是30%；
i：是计算后的数值的整数部分，这里计算左边（9-1）∗ 0.3 = 2.4, i = 2;
j：是计算后的小数部分，j = 0.4；
所以最后的结果为：
result = (1−j)∗arr[i]+j∗arr[i+1] = （1 - 0.4）× arr[2] + 0.4 x arr[2+1]
= 0.6 x 3 + 0.4 x 4
= 3.4
	
#### 统计数组中位数median(),平均数mean()
```python
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0)) # 行
print(np.median(a, axis=1)) # 列
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

'''
# 运行结果
5.0
[4. 5. 6.]
[2. 5. 8.]
5.0
[4. 5. 6.]
[2. 5. 8.]
'''
```
#### 统计数组中的加权平均值average()
```python
import numpy as np
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))
'''
# 运行结果
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print np.average(a)
print np.average(a,weights=wts)
'''
# 计算原理：np.average(a,weights=wts)=(1*1+2*2+3*3+4*4)/(1+2+3+4)=3.0
```

#### 统计数组中的标准差std()、方差()
- 反映数据的分散程度
```python
import numpy as np
a = np.array([1,2,3,4])
# 标准差
print(np.std(a))
# 平方差
print(np.var(a))

'''
运行结果：
1.118033988749895
1.25
'''
```
#### NumPy排序
- 使用sort()函数可以轻松搞定：
- sort(a, axis=-1, kind='quicksort', order=None)
- kind的值可以是quicksort、mergesort、heapsort等等
```python
import numpy as np
a = np.array([[4,3,2],[2,4,1]])
print(np.sort(a))
print(np.sort(a, axis=None)) # 不按照轴来排序，全部一起排
print(np.sort(a, axis=0)) # 按照行排列，小的在上，大的在下
print(np.sort(a, axis=1)) # 和axis为空的情况一直，但是实质是不同的

'''
运行结果：
[[2 3 4]
 [1 2 4]]
[1 2 2 3 4 4]
[[2 3 1]
 [4 4 2]]
[[2 3 4]
 [1 2 4]]
'''
```

## 总结
NumPy的使用比直接使用Python的List更加方便灵活，也更加快速。
> NumPy
    排序：1、快速排序
         2、合并排序
         3、堆排序
    定义数组：
         1、创建数组
         2、结构数组
    高效使用NumPy：
         1、为什么使用NumPy
         2、本地操作和隐式拷贝
    运算：
         1、算术运算
         2、统计运算

![](NumPy总结.jpg)

        


### 课后练习题目：
- 统计全班的成绩：在语文、数学、英语等中的平均成绩、最小成绩、最大成绩、方差、标准差。然后将这些人的总成绩排序输出：


```python
import numpy as np
persontype = np.dtype({
    'names':['name','chinese','english','math'],
    'formats':['S32','i','i','i']
})
peoples = np.array([("ZhangFei",66,65,30),("GuanYu",95,85,98),
                    ("ZhaoYun",93,92,96),("HuangZhong",90,88,77),
                    ("DianWei",80,90,90)],dtype=persontype)
chineses = peoples[:]['chinese']
englishs = peoples[:]['english']
maths = peoples[:]['math']
# 平均成绩
print(np.mean(chineses))
print(np.mean(englishs))
print(np.mean(maths))
# 输出最小值和最大值
print(np.amin(chineses))
print(np.amin(englishs))
print(np.amin(maths))
print(np.amax(chineses))
print(np.amax(englishs))
print(np.amax(maths))
# 计算方差和标准差
stdchinese = np.array(chineses)
print(np.std(stdchinese))
print(np.var(stdchinese))
stdenglish = np.array(englishs)
print(np.std(stdenglish))
print(np.var(stdenglish))
stdmath = np.array(maths)
print(np.std(stdmath))
print(np.var(stdmath))
# 排序
# ①所有成绩
a = np.array([chineses,englishs,maths])
print(np.sort(a))
# ②按照三科成绩之和降序排列
#用sorted函数进行排序
ranking = sorted(peoples,key=lambda x:x[1]+x[2]+x[3], reverse=True)
print(ranking)
```











