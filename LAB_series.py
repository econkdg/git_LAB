# ====================================================================================================
# series
# ====================================================================================================
# series: index - value, order
# ----------------------------------------------------------------------------------------------------
# import pandas

import pandas as pd
# ----------------------------------------------------------------------------------------------------
# series

s1 = pd.Series([10, 20, 30, 40])

s1.sum()  # sum
s1.mean()  # mean%

# list
s2 = pd.Series(['value1', 'value2', 'value3', 'value4'],
               index=['index1', 'index2', 'index3', 'index4'],
               name='series name')

# dictionary
s3 = pd.Series({'key1': 'value1', 'key2': 30,
               'key3': 'value3', 'key4': 'value4'})

# indexing using series
dic1 = {'key1': 'value1', 'key2': 30, 'key3': 'value3', 'key4': 'value4'}

s4 = pd.Series(dic1)
s5 = pd.Series(['value1', 'value2', 'value3', 'value4'])

print(s4)
print(s4['key2'])

print(s5[0])
print(s5[2:])
print(s5[:2])

print(s4 == 'value4')
s4[s4 == 'value4']
# ====================================================================================================
