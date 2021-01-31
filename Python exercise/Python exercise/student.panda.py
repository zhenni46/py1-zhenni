from pandas import Series, DataFrame
data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'])
print(df2)
print(df2.describe())
print(df2.var())
gradesum=df2.sum(axis=1)
print(gradesum)
df=DataFrame(gradesum)
print(df.sort_values(0))