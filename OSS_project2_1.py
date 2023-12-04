import pandas as pd

df = pd.read_csv("./2019_kbo_for_kaggle_v2.csv")

col = df[(df['year'] == 2015)]
col2 = df[(df['year'] == 2016)]
col3 = df[(df['year'] == 2017)]
col4 = df[(df['year'] == 2018)]

col5 = ['batter_name', 'H', 'avg', 'HR', 'OBP', 'year']

col_df = col[col5]
col_df2 = col2[col5]
col_df3 = col3[col5]
col_df4 = col4[col5]


# 1)
top10_H2015 = col_df.sort_values(by=['H'], ascending=False).head(10)
top10_H2016 = col_df2.sort_values(by=['H'], ascending=False).head(10)
top10_H2017 = col_df3.sort_values(by=['H'], ascending=False).head(10)
top10_H2018 = col_df4.sort_values(by=['H'], ascending=False).head(10)
print(top10_H2015['batter_name'])
print(top10_H2016['batter_name'])
print(top10_H2017['batter_name'])
print(top10_H2018['batter_name'])
print("-----------------------------------------")
top10_a2015 = col_df.sort_values(by=['avg'], ascending=False).head(10)
top10_a2016 = col_df2.sort_values(by=['avg'], ascending=False).head(10)
top10_a2017 = col_df3.sort_values(by=['avg'], ascending=False).head(10)
top10_a2018 = col_df4.sort_values(by=['avg'], ascending=False).head(10)
print(top10_a2015['batter_name'])
print(top10_a2016['batter_name'])
print(top10_a2017['batter_name'])
print(top10_a2018['batter_name'])
print("-----------------------------------------")
top10_HR2015 = col_df.sort_values(by=['HR'], ascending=False).head(10)
top10_HR2016 = col_df2.sort_values(by=['HR'], ascending=False).head(10)
top10_HR2017 = col_df3.sort_values(by=['HR'], ascending=False).head(10)
top10_HR2018 = col_df4.sort_values(by=['HR'], ascending=False).head(10)
print(top10_HR2015['batter_name'])
print(top10_HR2016['batter_name'])
print(top10_HR2017['batter_name'])
print(top10_HR2018['batter_name'])
print("-----------------------------------------")
top10_O2015 = col_df.sort_values(by=['OBP'], ascending=False).head(10)
top10_O2016 = col_df2.sort_values(by=['OBP'], ascending=False).head(10)
top10_O2017 = col_df3.sort_values(by=['OBP'], ascending=False).head(10)
top10_O2018 = col_df4.sort_values(by=['OBP'], ascending=False).head(10)
print(top10_O2015['batter_name'])
print(top10_O2016['batter_name'])
print(top10_O2017['batter_name'])
print(top10_O2018['batter_name'])
print("2)-----------------------------------------")
# 2)

df_1 = df[(df['cp'] == "포수") & (df['year'] == 2018)]
df_2 = df[(df['cp'] == "1루수") & (df['year'] == 2018)]
df_3 = df[(df['cp'] == "2루수") & (df['year'] == 2018)]
df_4 = df[(df['cp'] == "3루수") & (df['year'] == 2018)]
df_5 = df[(df['cp'] == "유격수") & (df['year'] == 2018)]
df_6 = df[(df['cp'] == "좌익수") & (df['year'] == 2018)]
df_7 = df[(df['cp'] == "중견수") & (df['year'] == 2018)]
df_8 = df[(df['cp'] == "우익수") & (df['year'] == 2018)]

for i in range(len(df_1)):
    vs = df_1.iloc[0]
    temp = df_1.iloc[i]
    if vs['war'] < temp['war']:
        df_1.iloc[0] = temp
df1 = df_1.iloc[0]
print(df1['batter_name'])
print("-----------------------------------------")
for i in range(len(df_2)):
    vs = df_2.iloc[0]
    temp = df_2.iloc[i]
    if vs['war'] < temp['war']:
        df_2.iloc[0] = temp
df2 = df_2.iloc[0]
print(df2['batter_name'])
print("-----------------------------------------")
for i in range(len(df_3)):
    vs = df_3.iloc[0]
    temp = df_3.iloc[i]
    if vs['war'] < temp['war']:
        df_3.iloc[0] = temp
df3 = df_3.iloc[0]
print(df3['batter_name'])
print("-----------------------------------------")
for i in range(len(df_4)):
    vs = df_4.iloc[0]
    temp = df_4.iloc[i]
    if vs['war'] < temp['war']:
        df_4.iloc[0] = temp
df4 = df_4.iloc[0]
print(df1['batter_name'])
print("-----------------------------------------")
for i in range(len(df_5)):
    vs = df_5.iloc[0]
    temp = df_5.iloc[i]
    if vs['war'] < temp['war']:
        df_5.iloc[0] = temp
df5 = df_5.iloc[0]
print(df5['batter_name'])
print("-----------------------------------------")
for i in range(len(df_6)):
    vs = df_6.iloc[0]
    temp = df_6.iloc[i]
    if vs['war'] < temp['war']:
        df_6.iloc[0] = temp
df6 = df_6.iloc[0]
print(df6['batter_name'])
print("-----------------------------------------")
for i in range(len(df_7)):
    vs = df_7.iloc[0]
    temp = df_7.iloc[i]
    if vs['war'] < temp['war']:
        df_7.iloc[0] = temp
df7 = df_7.iloc[0]
print(df7['batter_name'])
print("-----------------------------------------")
for i in range(len(df_8)):
    vs = df_8.iloc[0]
    temp = df_8.iloc[i]
    if vs['war'] < temp['war']:
        df_8.iloc[0] = temp
df8 = df_8.iloc[0]
print(df8['batter_name'])
print("3)-----------------------------------------")
# 3)
col3 = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']
dfS = df[col3].corr()['salary']
print(dfS)
# 연봉과 가장 관련성이 높은 것은 RBI이며 그외 R, H, HR, war가 연봉에 연관이 많다
# 반대로 SB가 연봉과 가장 연관이 없으며 avg, obp, SLG가 낮은 연관성을 보인다.