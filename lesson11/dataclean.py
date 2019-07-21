# encoding=utf-8
import pandas as pd
from pandas import Series, DataFrame
data = DataFrame(pd.read_excel('data1.xlsx'))
df = DataFrame(data)
# index 可以去掉
df1 = DataFrame(data,index=[0,1,2,3,4,5,6,7,8,9,10],
        columns=['No','name','Age','weight','M1','M2','M3','F1','F2','F3'])
# 在没有清洗之前，两种方式输出的数据是一样的，
# 清洗过后只是输出对应数据的修改，并没有修改源文件的数据，所以后期需要将清洗后的数据进行保存
print(df)
# print(df1)


# 1、想对df['Age']中缺失的数值使用平均年龄进行填充
# df['Age'].fillna(df['Age'].mean(), inplace = True)

# 2、使用高频的数据进行填充，可以先使用value_counts获取Age字段
# 的最高频次age_maxf,然后再对Age字段中的缺失的数据使用age_maxf进行填充：
# age_maxf = df['Age'].value_counts().index[0]
# df['Age'].fillna(age_maxf, inplace=True)

# 3、去除空行,注意，在前面如果填补上年龄了，就不算是空行了，所以要先注释，说明数据清洗需要一步步来
df.dropna(how='all', inplace=True)

# 4、统一单位
# 获取weight数据列中的单位为lbs的数据
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
print(df[rows_with_lbs])
# 将lbs转换为kgs，2.2lbs = 1kgs
for i, lbs_row in df[rows_with_lbs].iterrows():
    # 截取从头开始到倒数第三个字符之前，即去掉lbs
    weight = int(float(lbs_row['weight'][:-3])/2.2)
    df.at[i,'weight'] = '{}kgs'.format(weight)

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

print(df)

df.to_excel('data2.xlsx')


