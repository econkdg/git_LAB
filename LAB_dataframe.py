# ====================================================================================================
# dataframe
# ====================================================================================================
# dataframe: index - column - value
# ----------------------------------------------------------------------------------------------------
# dataframe

pd.DataFrame([10, 20, 30, 40, 50])

pd.DataFrame([[10, 20, 30, 40],
              ['value1', 'value2', 'value3', 'value4']])

df1 = pd.DataFrame([[1000, 'X1', '2021-01-01', 'Y1'],
                    [2000, 'X2', '2021-01-02', 'Y2'],
                    [3000, 'X3', '2021-01-03', 'Y3'],
                    [4000, 'X4', '2021-01-04', 'Y4']],
                   columns=['price', 'X', 'date', 'Y'])

print(df1)

# series type
df1['price']  # of bracket = 1

df1['price'].sum()  # sum
df1['price'].mean()  # mean

# dataframe type
df1[['price']]  # of bracket = 2
df1[['price', 'X']]
# ----------------------------------------------------------------------------------------------------
# import pandas & data

import pandas as pd

df1 = pd.read_csv('data1.csv')  # pd.read_excel('file name.xls')
# ----------------------------------------------------------------------------------------------------
# summarize

# data shape
df1.shape

# data type
df1.info()

# continuous data describe
df1.describe()

# head & tail
df1.head(5)  # data.tail(5)
# ----------------------------------------------------------------------------------------------------
# missing data

# isnull
df1.isnull().sum()  # df1.isnull()

# column's name
df1.columns
# ----------------------------------------------------------------------------------------------------
# pick columns

# pick the data
df1['구매금액']  # series

df1['구매금액'].sum()
df1['구매금액'].describe()  # series

df1[['구매금액', '성별']]  # dataframe
# df1['구매금액', '성별'] -> error (dataframe: index + value + column)

df2 = df1[['구매금액', '성별']]
print(df2)
# ----------------------------------------------------------------------------------------------------
# pick rows

# data shape
print(df1.shape)

# data head
df1.head(2)

# range index
df1.index

# values
df1.values

# describe: continuous data 5 number summary
df1.describe()

# info: summary of DataFrame
df1.info()

# pick columns
df1[['구매금액', '물품대분류', '물품중분류']]

# iloc[index]
df1.iloc[0]  # series
df1.iloc[10]  # 10th
df1.iloc[-1]  # 1st from the last

# iloc[range index]
df1.iloc[0:11]
df1.iloc[:100]
df1.iloc[100:]

df2 = df1.iloc[100:]
df2.shape
# ----------------------------------------------------------------------------------------------------
# sort

# descending sort
df1.sort_values(by='구매금액', ascending=False)

# ascending sort(default)
df1.sort_values(by='구매금액')

# sort by two keys(descending, ascending, top 10 data)
df1.sort_values(by=['구매수량', '연령'], ascending=[False, True]).iloc[:10]
# ----------------------------------------------------------------------------------------------------
# filter

# value_counts
df1['연령대'].value_counts()
df1['성별'].value_counts()

# loc[cond]
df1['연령대'] == '40대'  # series

cond1 = (df1['연령대'] == '40대')
df1.loc[cond1]

cond2 = (df1['연령대'] != '40대')
df1.loc[cond2]

df1.loc[cond1].shape

# loc[~cond]
cond1 = (df1['연령대'] == '40대')
df1.loc[~cond1]

# multiple conditions
cond1 = (df1['연령대'] == '4o대')
cond2 = (df1['성별'] == '남')

df1.loc[cond1 & cond2]  # and
df1.loc[cond1 | cond2]  # or
# ----------------------------------------------------------------------------------------------------
# save

# practice
# 1. pick rows by '연령대': 30대이하, '성별': 여
# 2. sort sub-data by '구매금액'
# 3. save file

cond1 = (df1['연령대'] == '30대이하')
cond2 = (df1['성별'] == '여')

df3 = df1[cond1 & cond2].sort_values(by='구매금액', ascending=False)

df3.shape

df3.to_excel('result.xlsx', encoding='cp949')  # encoding='cp949': 한글 깨짐 방지
# ====================================================================================================
