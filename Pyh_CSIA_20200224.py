
"""
import pandas as pd

serie = pd.Series(['Java', 'Python', 'JavaScript'])
print(serie)

languages = ['Java', 'Python', 'JavaScript']
ranking = [3, 1, 2]
serie = pd.Series(ranking, index=languages)
print(serie['Java'])

names = ['Tony', 'Amy', 'Joe']
followers = [77, 45, 12]
serie = pd.Series(followers, index=names)
print(serie['Amy'])

movies = {
    '名稱': ['名偵探柯南', '復仇者聯盟', '那些年'],
    '票房金額（新台幣）': [1452324, 2324739, 1416601],
    '類別': ['動畫', '動作', '文藝']
}

df = pd.DataFrame(movies)

print(df.info())
print(df.describe())
print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.values)

for index, row in df.iterrows():
    print(row['名稱'], row['類別'])

df.loc[0, '名稱']
df.loc[0:1, '名稱']
df.loc[0:1, '名稱':'類別']

df[df['票房金額（新台幣）'] > 2000000]
df[df['類別'] == '動畫']

# 可使用 encoding 避免編碼問題
# df = pd.read_csv('./_data/youbike_data.csv', encoding='utf-8')
df = pd.read_csv('./_data/YouBike_20200224.csv', encoding='utf-8')
df.to_excel('./_data/YouBike_20200224.xlsx')

print(df.info())
print(df.describe())
print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.values)

# 使用別名 plt
import matplotlib.pyplot as plt

# 長條圖
# X 軸
stock_list = ['2031', '2341', '2342', '2345']
# Y 軸
volumes = [34123, 122212, 41907, 3115987]

plt.bar(stock_list, volumes)
plt.show()
plt.savefig('./_img/plt_bar.png')

# 折線圖
# X 軸
stock_list = ['2031', '2341', '2342', '2345']
# Y 軸
volumes = [34123, 122212, 41907, 3115987]

plt.plot(stock_list, volumes)
plt.show()
plt.savefig('./_img/plt_plot.png')

# 圓餅圖
# X 軸
stock_list = ['2031', '2341', '2342', '2345']
# Y 軸
volumes = [34123, 122212, 41907, 3115987]

plt.pie(volumes, labels=stock_list)
plt.show()
plt.savefig('./_img/plt_pie.png')

import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 資料
df = pd.read_csv('./_data/performance.csv')

# 選取所有列的 date, year_revenue 欄資料
data = df.loc[:, ['date', 'year_revenue']]
# 將 date 設為 index，要當作 X 軸使用
data = data.set_index('date')

print('data', data)

# 產生 line chart
fig = data.plot(kind='line').get_figure()
plt.title('stock performance')
fig.savefig('./_img/plt_Stock.png')

# 產生 bar chart
fig = data.plot(kind='bar').get_figure()
plt.title('stock performance')
fig.savefig('./_img/plt_Perfor.png')


import pandas as pd
import matplotlib.pyplot as plt

# 下載 stock_data.csv, 使用 DataFrame 物件的 read_csv 方法讀入
df = pd.read_csv('./_data/STOCK_DAY_ALL.csv')

print(df.info())
print(df.describe())
print(df.head(5))
print(df.tail(5))

# 取出 第 2-7 筆資料的 證券代號,證券名稱,收盤價,成交筆數 值
select = df.loc[1:6, ['證券代號', '證券名稱', '收盤價','成交筆數']]
print(select)
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'./_font/noto-cjk-master/NotoSansCJK-Black.ttc')

# 下載 stock_data.csv, 使用 DataFrame 物件的 read_csv 方法讀入
df = pd.read_csv('./_data/STOCK_DAY_ALL.csv', encoding='utf-8')

# 取出 前 6 筆資料的 證券代號, 收盤價 值繪製折線圖
data = df.loc[0:5, ['證券代號', '收盤價']]

# X 軸為 證券代號，Y 軸為 收盤價
x = data['證券代號']
y = data['收盤價'].astype('float')

# 折線圖
plt.figure(figsize=(7,5))
plt.plot(x, y)
plt.title('個股日成交資訊', fontproperties=myfont)
plt.xlabel('證券代號', fontproperties=myfont)
plt.ylabel('收盤價', fontproperties=myfont)
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig('./_img/plt_stock_20200224.png')


