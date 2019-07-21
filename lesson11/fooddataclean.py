# encoding=utf-8
# 这个文件考虑到使用“完全合一”的原则从头到尾清理数据存在问题，
# 所以这里是使用的顺序是不同“完全合一”的乱序
import pandas as pd
from pandas import Series, DataFrame
data = DataFrame(pd.read_excel('food1.xlsx'))
df = DataFrame(data)
# 在没有清洗之前，两种方式输出的数据是一样的，
# 清洗过后只是输出对应数据的修改，并没有修改源文件的数据，所以后期需要将清洗后的数据进行保存
print(df)


# 1、去除空行,参数how=all的意思是行内所有值都为空的时候才删除
# df.dropna(how='all', inplace=True)
# 没有参数的时候就是行内有空值NaN的时候都删掉,
# 删掉有NaN的的Bacon
df = df.dropna()
# 删除之后需要重新调整index，使其有序
df.index = range(len(df)) # reset index

# 2、标题行首字母大写
df.columns = df.columns.str.title()

# 3、每一行的第一列首字母大写
# 如果需要操作行的元素的话应该这样操作
df['Food'] = df['Food'].str.title()

# 4、不能简单去掉重复行，这是份菜单，
# 为了保险，值应该取平均值之后再删除重复的行
# df.loc[0,'Ounces'] 意思是定位到Ounces列的第一行的值，1：第二行，2：第三行
df['Ounces'] = df['Ounces'].apply(lambda a:abs(a))
df.loc[0,'Ounces'] = df[df['Food'].isin(['Bacon'])].mean()['Ounces']
# 输出第四行的Bacon
df.drop(df.index[4],inplace=True)
df.index = range(len(df)) # reset index
# df.drop_duplicates(['Food'],inplace=True)


# 5、继续处理重复行：Pastrami
# 获取pastrami的平均值,赋值给第一个值，同时删除第二个值,但是第二个是负值，
# 不合法，也不能简单的求平均值，先转成正数，再算平均值,使用apply函数和匿名函数
df['Ounces'] = df['Ounces'].apply(lambda a:abs(a))
df.loc[2,'Ounces'] = df[df['Food'].isin(['Pastrami'])].mean()['Ounces']
df.drop(df.index[4],inplace=True)
# 重置index
df.index = range(len(df))

print(df)

df.to_excel('food2.xlsx')
