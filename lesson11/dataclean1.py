# encoding=utf-8
# 这个文件考虑到使用“完全合一”的原则从头到尾清理数据存在问题，
# 所以这里是使用的顺序是不同“完全合一”的乱序
import pandas as pd
from pandas import Series, DataFrame
data = DataFrame(pd.read_excel('data1.xlsx'))
df = DataFrame(data)
# 在没有清洗之前，两种方式输出的数据是一样的，
# 清洗过后只是输出对应数据的修改，并没有修改源文件的数据，所以后期需要将清洗后的数据进行保存
print(df)


# 3、去除空行,注意，在前面如果填补上年龄了，就不算是空行了，所以要先注释，说明数据清洗需要一步步来
df.dropna(how='all', inplace=True)


# 2、使用高频的数据进行填充，可以先使用value_counts获取Age字段
# 的最高频次age_maxf,然后再对Age字段中的缺失的数据使用age_maxf进行填充：
age_maxf = df['Age'].value_counts().index[0]
df['Age'].fillna(age_maxf, inplace=True)


# 4、统一单位
# 获取weight数据列中的单位为lbs的数据
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
print(df[rows_with_lbs])
# 将lbs转换为kgs，2.2lbs = 1kgs
for i, lbs_row in df[rows_with_lbs].iterrows():
    # 截取从头开始到倒数第三个字符之前，即去掉lbs
    weight = int(float(lbs_row['weight'][:-3])/2.2)
    df.at[i,'weight'] = '{}kgs'.format(weight)

# 先统一体重单位，想对df['weight']中缺失的数值使用平均体重进行填充
rows_with_kgs = df['weight'].str.contains('kgs').fillna(False)
for i, kgs_row in df[rows_with_kgs].iterrows():
    # 先将kgs去掉，转换成float，计算平均值，再添加kgs
    weight = int(float(kgs_row['weight'][:-3]))
    df.at[i,'weight'] = weight

# 转换为int之后使用平均值填充
df['weight'].fillna(df['weight'].mean(), inplace = True)


# 4、唯一性
# 处理一列有多个参数，姓名列（name）包含了两个参数：Firstname和Lastname，为了使得数据整洁目的，将name拆分成
# Firstname和Lastname两个字段。
# 切分名字，删除源数据列
df[['first_name','last_name']] = df['name'].str.split(expand=True)
df.drop('name',axis=1,inplace=True)

# 处理重复数据：删除重复数据行
df.drop_duplicates(['first_name','last_name'],inplace=True)

# 3、合理性
# 处理：删除非ASCII字符
df['first_name'].replace({r'[^\x00-\x7F]+':''},regex=True, inplace=True)
df['last_name'].replace({r'[^\x00-\x7F]+':''},regex=True, inplace=True)


# 重命名column，使得列表适合需要
df.rename(columns={'weight':'Weight(kgs)','first_name':'First_Name','last_name':'Last_Name'},inplace=True)

# 列名重新排序
cols=['No','First_Name','Last_Name','Age','Weight(kgs)','M1','M2','M3','F1','F2','F3']
df = df.filter(cols, axis=1)

# 删除原来的No列
df.drop('No',axis=1,inplace=True)

# 重置index
df.index = range(len(df))

print(df)

df.to_excel('data3.xlsx')


