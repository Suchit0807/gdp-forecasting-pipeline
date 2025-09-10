# Auto-generated from notebook for reproducible results
from pathlib import Path
def __auto_show__(x, n=5):
    try:
        import pandas as pd
        if isinstance(x, pd.DataFrame):
            print(x.head(n).to_string(index=False))
            return
        if isinstance(x, pd.Series):
            print(x.head(n).to_string())
            return
    except Exception:
        pass
    try:
        from pprint import pprint
        pprint(x)
    except Exception:
        print(x)


# --- Markdown cell 2 ---
# # Importing Necessary Libraries

# --- Code cell 3 ---
import pandas as pd
import matplotlib.pyplot as plt

# --- Markdown cell 4 ---
# # Core CPI

# --- Code cell 5 ---
df = pd.read_excel("/work/Core CPI, seas. adj..xlsx")
# df.head()
__auto_show__(df.head())

# --- Code cell 6 ---
df = df.rename(columns = {'Unnamed: 0':'Year'})
# df.head()
__auto_show__(df.head())

# --- Code cell 7 ---
df1 = df[['Year', 'United States', 'United Kingdom', 'Japan', 'China']]
# df1.head()
__auto_show__(df1.head())

# --- Code cell 8 ---
# df1.isnull().sum()
__auto_show__(df1.isnull().sum())

# --- Code cell 9 ---
# df1.tail()
__auto_show__(df1.tail())

# --- Code cell 10 ---
df1 = df1.drop([0, df1.index[-1]])

# --- Code cell 11 ---
# df1.isnull().sum()
__auto_show__(df1.isnull().sum())

# --- Code cell 12 ---
def fill_missing_values(df1, column):
    First_Year = df1[column].first_valid_index()
    Last_Year = df1[column].last_valid_index()

    trend = (df1.loc[Last_Year, column] - df1.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df1[df1[column].isnull()].index
    df1.loc[missing_years, column] = df1.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df1, 'China')

# print(df1)
__auto_show__(print(df1))

# --- Code cell 13 ---
df1['Year'] = df1['Year'].astype(int)
df1 = df1.set_index('Year')

# --- Code cell 14 ---
# df1.describe()
__auto_show__(df1.describe())

# --- Markdown cell 15 ---
# # Imports Merchandise

# --- Code cell 16 ---
df = pd.read_excel("/work/Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx")
# df.head()
__auto_show__(df.head())

# --- Code cell 17 ---
df = df.rename(columns = {'Unnamed: 0':'Year'})
# df.head()
__auto_show__(df.head())

# --- Code cell 18 ---
df2 = df[['Year', 'United States', 'United Kingdom', 'Japan', 'China']]
# df2.head()
__auto_show__(df2.head())

# --- Code cell 19 ---
# df2.isnull().sum()
__auto_show__(df2.isnull().sum())

# --- Code cell 20 ---
df2 = df2.drop([0, df2.index[-1]])

# --- Code cell 21 ---
# df2.isnull().sum()
__auto_show__(df2.isnull().sum())

# --- Code cell 22 ---
# df2.head()
__auto_show__(df2.head())

# --- Code cell 23 ---
df2['Year'] = df2['Year'].astype(int)
# df2.set_index('Year', inplace = True)
__auto_show__(df2.set_index('Year', inplace = True))

# --- Code cell 24 ---
# df2.head()
__auto_show__(df2.head())

# --- Code cell 25 ---
# df2.describe()
__auto_show__(df2.describe())

# --- Markdown cell 26 ---
# # Exports Merchandise

# --- Code cell 27 ---
df = pd.read_excel("/work/Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx")
# df.head()
__auto_show__(df.head())

# --- Code cell 28 ---
df = df.rename(columns = {'Unnamed: 0':'Year'})
# df.head()
__auto_show__(df.head())

# --- Code cell 29 ---
df3 = df[['Year', 'United States', 'United Kingdom', 'Japan', 'China']]
# df3.head()
__auto_show__(df3.head())

# --- Code cell 30 ---
# df3.isnull().sum()
__auto_show__(df3.isnull().sum())

# --- Code cell 31 ---
df3 = df3.drop([0, df3.index[-1]])

# --- Code cell 32 ---
# df3.isnull().sum()
__auto_show__(df3.isnull().sum())

# --- Code cell 33 ---
# df3.set_index('Year', inplace = True)
__auto_show__(df3.set_index('Year', inplace = True))

# --- Code cell 34 ---
# df3.head()
__auto_show__(df3.head())

# --- Code cell 35 ---
# df3.describe()
__auto_show__(df3.describe())

# --- Markdown cell 36 ---
# # Health Expenditure

# --- Code cell 37 ---
df = pd.read_excel("/work/Health Expenditure Final.xlsx")
# df
__auto_show__(df)

# --- Code cell 38 ---
df4 = df.rename(columns = {'Unnamed: 0':'Year'})
# df4.head()
__auto_show__(df4.head())

# --- Code cell 39 ---
# df4.isnull().sum()
__auto_show__(df4.isnull().sum())

# --- Code cell 40 ---
def fill_missing_values(df4, column):
    First_Year = df4[column].first_valid_index()
    Last_Year = df4[column].last_valid_index()

    trend = (df4.loc[Last_Year, column] - df4.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df4[df4[column].isnull()].index
    df4.loc[missing_years, column] = df4.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df4, 'China')

# print(df4)
__auto_show__(print(df4))

# --- Code cell 41 ---
df4['Year']=df4['Year'].astype(int)
# df4.set_index('Year', inplace = True)
__auto_show__(df4.set_index('Year', inplace = True))

# --- Code cell 42 ---
# df4.describe()
__auto_show__(df4.describe())

# --- Markdown cell 43 ---
# # Unemployment Rate

# --- Code cell 44 ---
df = pd.read_excel("/work/Unemployment Rate, seas. adj..xlsx")
# df
__auto_show__(df)

# --- Code cell 45 ---
df5 = df.rename(columns = {'Unnamed: 0':'Year'})
# df5.head()
__auto_show__(df5.head())

# --- Code cell 46 ---
df5 = df5[['Year', 'United States', 'United Kingdom', 'Japan', 'Hong Kong SAR, China']]
# df5.head()
__auto_show__(df5.head())

# --- Code cell 47 ---
# df5.isnull().sum()
__auto_show__(df5.isnull().sum())

# --- Code cell 48 ---
df5 = df5.drop([0, df5.index[-1]])

# --- Code cell 49 ---
# df5.head()
__auto_show__(df5.head())

# --- Code cell 50 ---
# df5.isnull().sum()
__auto_show__(df5.isnull().sum())

# --- Code cell 51 ---
df5['Year']=df5['Year'].astype(int)
# df5.set_index('Year',inplace=True)
__auto_show__(df5.set_index('Year',inplace=True))

# --- Code cell 52 ---
# df5.head()
__auto_show__(df5.head())

# --- Code cell 53 ---
df5 = df5.rename(columns={'Hong Kong SAR, China':'China'})

# --- Code cell 54 ---
# df5.head()
__auto_show__(df5.head())

# --- Markdown cell 55 ---
# # GDP

# --- Code cell 56 ---
df = pd.read_excel("/work/GDP at market prices, current US$, millions, seas. adj..xlsx")
# df.head()
__auto_show__(df.head())

# --- Code cell 57 ---
df6 = df.rename(columns = {'Unnamed: 0':'Year'})
# df6.head()
__auto_show__(df6.head())

# --- Code cell 58 ---
df6 = df6[['Year', 'United States', 'United Kingdom', 'Japan', 'China']]
# df6.head()
__auto_show__(df6.head())

# --- Code cell 59 ---
# df6.isnull().sum()
__auto_show__(df6.isnull().sum())

# --- Code cell 60 ---
df6 = df6.drop([0, df6.index[-1]])

# --- Code cell 61 ---
# df6.isnull().sum()
__auto_show__(df6.isnull().sum())

# --- Code cell 62 ---
df6['Year']=df6['Year'].astype(int)
# df6.set_index('Year',inplace=True)
__auto_show__(df6.set_index('Year',inplace=True))

# --- Code cell 63 ---
# df6.describe()
__auto_show__(df6.describe())

# --- Markdown cell 64 ---
# # Manufacturing (% of GDP)

# --- Code cell 65 ---
df = pd.read_excel("/work/Manufacturing Data (% of GDP).xls")
# df.head()
__auto_show__(df.head())

# --- Code cell 66 ---
# df.drop(columns = ["Country Code", "Indicator Name", "Indicator Code"], inplace = True)
__auto_show__(df.drop(columns = ["Country Code", "Indicator Name", "Indicator Code"], inplace = True))

# --- Code cell 67 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 68 ---
# df.set_index("Country Name", inplace = True)
__auto_show__(df.set_index("Country Name", inplace = True))

# --- Code cell 69 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 70 ---
transposed_df = df.T

# --- Code cell 71 ---
# transposed_df.head()
__auto_show__(transposed_df.head())

# --- Code cell 72 ---
df7 = transposed_df[["United States","United Kingdom","Japan","China"]]

# --- Code cell 73 ---
# df7.head()
__auto_show__(df7.head())

# --- Code cell 74 ---
df7.index.name = 'Year'

# --- Code cell 75 ---
# df7.head()
__auto_show__(df7.head())

# --- Code cell 76 ---
df7.columns.name = None

# --- Code cell 77 ---
# df7.head()
__auto_show__(df7.head())

# --- Code cell 78 ---
# df7.isnull().sum()
__auto_show__(df7.isnull().sum())

# --- Code cell 79 ---
df7 = df7.loc["1994": "2022"]

# --- Code cell 80 ---
# df7
__auto_show__(df7)

# --- Code cell 81 ---
# df7.isnull().sum()
__auto_show__(df7.isnull().sum())

# --- Code cell 82 ---
def fill_missing_values(df7, column):
    df7.index = df7.index.astype(int)
    First_Year = df7[column].first_valid_index()
    Last_Year = df7[column].last_valid_index()

    trend = (df7.loc[Last_Year, column] - df7.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df7[df7[column].isnull()].index
    df7.loc[missing_years, column] = df7.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df7, 'China')
fill_missing_values(df7, 'Japan')
fill_missing_values(df7, 'United States')

# print(df7)
__auto_show__(print(df7))

# --- Code cell 83 ---
# df7.describe()
__auto_show__(df7.describe())

# --- Markdown cell 84 ---
# # Political Stability (NoViolence)

# --- Code cell 85 ---
df = pd.read_excel("/work/wgidataset Final.xlsx", sheet_name = 'Political StabilityNoViolence')
# df.head()
__auto_show__(df.head())

# --- Code cell 86 ---
df = df.rename(columns = {'Unnamed: 0':'Country'})

# --- Code cell 87 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 88 ---
# df.set_index('Country', inplace = True)
__auto_show__(df.set_index('Country', inplace = True))

# --- Code cell 89 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 90 ---
df_transposed = df.T

# --- Code cell 91 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 92 ---
df_transposed.index.name = 'Year'

# --- Code cell 93 ---
df_transposed.columns.name = None

# --- Code cell 94 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 95 ---
df_new = df_transposed.T

# --- Code cell 96 ---
# df_new.head()
__auto_show__(df_new.head())

# --- Code cell 97 ---
import numpy as np

# --- Code cell 98 ---
df_new.insert(1, '1997', np.nan)
df_new.insert(3, '1999', np.nan)
# df_new.insert(5, '2001', np.nan)
__auto_show__(df_new.insert(5, '2001', np.nan))

# --- Code cell 99 ---
# df_new.head()
__auto_show__(df_new.head())

# --- Code cell 100 ---
missing_data = pd.DataFrame(index = df.index, columns = ['1994', '1995'])

df_new = pd.concat([missing_data, df_new], axis = 1)

df_new = df_new.sort_index()

# print(df_new)
__auto_show__(print(df_new))

# --- Code cell 101 ---
# df_new.head()
__auto_show__(df_new.head())

# --- Code cell 102 ---
df8 = df_new.T

# --- Code cell 103 ---
# df8.head()
__auto_show__(df8.head())

# --- Code cell 104 ---
df8.index.name = 'Year'

# --- Code cell 105 ---
df8 = df8[['United States','United Kingdom','Japan','China']]

# --- Code cell 106 ---
# df8.isnull().sum()
__auto_show__(df8.isnull().sum())

# --- Code cell 107 ---
def fill_missing_values(df8, column):
    df8.index = df8.index.astype(int)
    First_Year = df8[column].first_valid_index()
    Last_Year = df8[column].last_valid_index()

    trend = (df8.loc[Last_Year, column] - df8.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df8[df8[column].isnull()].index
    df8.loc[missing_years, column] = df8.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df8, 'China')
fill_missing_values(df8, 'Japan')
fill_missing_values(df8, 'United States')
fill_missing_values(df8, 'United Kingdom')

# print(df8)
__auto_show__(print(df8))

# --- Code cell 108 ---
# df8.isnull().sum()
__auto_show__(df8.isnull().sum())

# --- Code cell 109 ---
# df8.describe()
__auto_show__(df8.describe())

# --- Code cell 110 ---
df8['United States'] = df8['United States'].astype(float)
df8['United Kingdom'] = df8['United Kingdom'].astype(float)
df8['Japan'] = df8['Japan'].astype(float)
df8['China'] = df8['China'].astype(float)

# --- Code cell 111 ---
# df8.describe()
__auto_show__(df8.describe())

# --- Markdown cell 112 ---
# # FDI Net Inflows

# --- Code cell 113 ---
df = pd.read_excel("/work/FDI Net Inflows.xlsx")
# df.head()
__auto_show__(df.head())

# --- Code cell 114 ---
# df.set_index('CountryName', inplace = True)
__auto_show__(df.set_index('CountryName', inplace = True))

# --- Code cell 115 ---
# df
__auto_show__(df)

# --- Code cell 116 ---
df_Transposed = df.T

# --- Code cell 117 ---
# df_Transposed.head()
__auto_show__(df_Transposed.head())

# --- Code cell 118 ---
df_Transposed.index.name = 'Year'

# --- Code cell 119 ---
# df_Transposed
__auto_show__(df_Transposed)

# --- Code cell 120 ---
df_Transposed.columns.name = None

# --- Code cell 121 ---
# df_Transposed
__auto_show__(df_Transposed)

# --- Code cell 122 ---
df9 = df_Transposed[['United States','United Kingdom','Japan','China']]

# --- Code cell 123 ---
# df9.head()
__auto_show__(df9.head())

# --- Code cell 124 ---
df9.index = pd.to_numeric(df9.index)
df9 = df9.loc[1994:2022]
# df9.head()
__auto_show__(df9.head())

# --- Code cell 125 ---
# df9.isnull().sum()
__auto_show__(df9.isnull().sum())

# --- Code cell 126 ---
# df9.describe()
__auto_show__(df9.describe())

# --- Markdown cell 127 ---
# # Government Final Consumption

# --- Code cell 128 ---
df = pd.read_excel("/work/General government final consumption expenditure (current US$).xls")
# df.head()
__auto_show__(df.head())

# --- Code cell 129 ---
# df.drop(columns = ['Country Code', 'Indicator Name', 'Indicator Code'], inplace = True)
__auto_show__(df.drop(columns = ['Country Code', 'Indicator Name', 'Indicator Code'], inplace = True))

# --- Code cell 130 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 131 ---
# df.set_index("Country Name", inplace = True)
__auto_show__(df.set_index("Country Name", inplace = True))

# --- Code cell 132 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 133 ---
Transposed_df = df.T

# --- Code cell 134 ---
# Transposed_df.head()
__auto_show__(Transposed_df.head())

# --- Code cell 135 ---
df10 = Transposed_df[["United States","United Kingdom","Japan","China"]]

# --- Code cell 136 ---
# df10.head()
__auto_show__(df10.head())

# --- Code cell 137 ---
df10.index.name = 'Year'

# --- Code cell 138 ---
df10.columns.name = None

# --- Code cell 139 ---
# df10.head()
__auto_show__(df10.head())

# --- Code cell 140 ---
# df10.isnull().sum()
__auto_show__(df10.isnull().sum())

# --- Code cell 141 ---
df10 = df10.loc['1994':'2022']

# --- Code cell 142 ---
# df10.head()
__auto_show__(df10.head())

# --- Code cell 143 ---
# df10.isnull().sum()
__auto_show__(df10.isnull().sum())

# --- Code cell 144 ---
# df10.tail()
__auto_show__(df10.tail())

# --- Code cell 145 ---
def fill_missing_values(df10, column):
    df10.index = df10.index.astype(int)
    First_Year = df10[column].first_valid_index()
    Last_Year = df10[column].last_valid_index()

    trend = (df10.loc[Last_Year, column] - df10.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df10[df10[column].isnull()].index
    df10.loc[missing_years, column] = df10.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df10, 'United States')

# print(df10)
__auto_show__(print(df10))

# --- Code cell 146 ---
# df10.describe()
__auto_show__(df10.describe())

# --- Markdown cell 147 ---
# # Exchange Rate

# --- Code cell 148 ---
df = pd.read_excel("/work/Exchange rate, new LCU per USD extended backward, period average.xlsx")
# df.head()
__auto_show__(df.head())

# --- Code cell 149 ---
df = df.rename(columns = {'Unnamed: 0':'Year'})
# df.head()
__auto_show__(df.head())

# --- Code cell 150 ---
df11 = df[['Year','United States','United Kingdom','Japan','China']]

# --- Code cell 151 ---
# df11.head()
__auto_show__(df11.head())

# --- Code cell 152 ---
# df11.isnull().sum()
__auto_show__(df11.isnull().sum())

# --- Code cell 153 ---
# df11.tail()
__auto_show__(df11.tail())

# --- Code cell 154 ---
df11 = df11.drop([0, df11.index[-1]])

# --- Code cell 155 ---
# df11.isnull().sum()
__auto_show__(df11.isnull().sum())

# --- Code cell 156 ---
# df11.set_index('Year', inplace = True)
__auto_show__(df11.set_index('Year', inplace = True))

# --- Code cell 157 ---
# df11.head()
__auto_show__(df11.head())

# --- Code cell 158 ---
# df11.describe()
__auto_show__(df11.describe())

# --- Markdown cell 159 ---
# # Political Stability (Regulatory Quality)

# --- Code cell 160 ---
df = pd.read_excel("/work/wgidataset Final.xlsx", sheet_name = 'RegulatoryQuality')

# --- Code cell 161 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 162 ---
df = df.rename(columns = {'Unnamed: 0':'Country'})
# df.head()
__auto_show__(df.head())

# --- Code cell 163 ---
df.set_index("Country", inplace = True)
# df.head()
__auto_show__(df.head())

# --- Code cell 164 ---
df_transposed = df.T

# --- Code cell 165 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 166 ---
df_transposed.index.name = 'Year'

# --- Code cell 167 ---
df_transposed.columns.name = None

# --- Code cell 168 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 169 ---
df_New = df_transposed.T

# --- Code cell 170 ---
# df_New.head()
__auto_show__(df_New.head())

# --- Code cell 171 ---
df_New.insert(1, '1997', np.nan)
df_New.insert(3, '1999', np.nan)
# df_New.insert(5, '2001', np.nan)
__auto_show__(df_New.insert(5, '2001', np.nan))

# --- Code cell 172 ---
# df_New.head()
__auto_show__(df_New.head())

# --- Code cell 173 ---
missing_data = pd.DataFrame(index = df.index, columns = ['1994', '1995'])

df_New = pd.concat([missing_data, df_New], axis = 1)

df_New = df_New.sort_index()

# print(df_New)
__auto_show__(print(df_New))

# --- Code cell 174 ---
df12 = df_New.T

# --- Code cell 175 ---
# df12
__auto_show__(df12)

# --- Code cell 176 ---
df12.index.name = 'Year'

# --- Code cell 177 ---
df12 = df12[['United States','United Kingdom','Japan','China']]

# --- Code cell 178 ---
# df12.isnull().sum()
__auto_show__(df12.isnull().sum())

# --- Code cell 179 ---
def fill_missing_values(df12, column):
    df12.index = df12.index.astype(int)
    First_Year = df12[column].first_valid_index()
    Last_Year = df12[column].last_valid_index()

    trend = (df12.loc[Last_Year, column] - df12.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df12[df12[column].isnull()].index
    df12.loc[missing_years, column] = df12.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df12, 'China')
fill_missing_values(df12, 'Japan')
fill_missing_values(df12, 'United States')
fill_missing_values(df12, 'United Kingdom')

# print(df12)
__auto_show__(print(df12))

# --- Code cell 180 ---
df12['United States'] = df12['United States'].astype(float)
df12['United Kingdom'] = df12['United Kingdom'].astype(float)
df12['Japan'] = df12['Japan'].astype(float)
df12['China'] = df12['China'].astype(float)

# --- Code cell 181 ---
# df12.describe()
__auto_show__(df12.describe())

# --- Markdown cell 182 ---
# # Political Stability (Control of Corruption)

# --- Code cell 183 ---
df = pd.read_excel("/work/wgidataset Final.xlsx", sheet_name = 'ControlofCorruption')
# df.head()
__auto_show__(df.head())

# --- Code cell 184 ---
df = df.rename(columns = {'Unnamed: 0':'Country'})
# df.head()
__auto_show__(df.head())

# --- Code cell 185 ---
df.set_index("Country", inplace = True)
# df.head()
__auto_show__(df.head())

# --- Code cell 186 ---
df_transposed = df.T

# --- Code cell 187 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 188 ---
df_transposed.index.name = 'Year'

# --- Code cell 189 ---
df_transposed.columns.name = None

# --- Code cell 190 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 191 ---
df_New = df_transposed.T

# --- Code cell 192 ---
# df_New.head()
__auto_show__(df_New.head())

# --- Code cell 193 ---
df_New.insert(1, '1997', np.nan)
df_New.insert(3, '1999', np.nan)
# df_New.insert(5, '2001', np.nan)
__auto_show__(df_New.insert(5, '2001', np.nan))

# --- Code cell 194 ---
# df_New.head()
__auto_show__(df_New.head())

# --- Code cell 195 ---
missing_data = pd.DataFrame(index = df.index, columns = ['1994', '1995'])

df_New = pd.concat([missing_data, df_New], axis = 1)

df_New = df_New.sort_index()

# print(df_New)
__auto_show__(print(df_New))

# --- Code cell 196 ---
df13 = df_New.T

# --- Code cell 197 ---
# df13
__auto_show__(df13)

# --- Code cell 198 ---
df13.index.name = 'Year'

# --- Code cell 199 ---
df13 = df13[['United States','United Kingdom','Japan','China']]

# --- Code cell 200 ---
# df13.isnull().sum()
__auto_show__(df13.isnull().sum())

# --- Code cell 201 ---
def fill_missing_values(df13, column):
    df13.index = df13.index.astype(int)
    First_Year = df13[column].first_valid_index()
    Last_Year = df13[column].last_valid_index()

    trend = (df13.loc[Last_Year, column] - df13.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df13[df13[column].isnull()].index
    df13.loc[missing_years, column] = df13.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df13, 'China')
fill_missing_values(df13, 'Japan')
fill_missing_values(df13, 'United States')
fill_missing_values(df13, 'United Kingdom')

# print(df13)
__auto_show__(print(df13))

# --- Code cell 202 ---
df13['United States'] = df13['United States'].astype(float)
df13['United Kingdom'] = df13['United Kingdom'].astype(float)
df13['Japan'] = df13['Japan'].astype(float)
df13['China'] = df13['China'].astype(float)

# --- Code cell 203 ---
# df13.describe()
__auto_show__(df13.describe())

# --- Markdown cell 204 ---
# # Political Stability (Government Effectiveness)

# --- Code cell 205 ---
df = pd.read_excel("/work/wgidataset Final.xlsx", sheet_name = 'GovernmentEffectiveness')

# --- Code cell 206 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 207 ---
df = df.rename(columns = {'Unnamed: 0':'Country'})
# df.head()
__auto_show__(df.head())

# --- Code cell 208 ---
df.set_index("Country", inplace = True)
# df.head()
__auto_show__(df.head())

# --- Code cell 209 ---
df_transposed = df.T

# --- Code cell 210 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 211 ---
df_transposed.index.name = 'Year'

# --- Code cell 212 ---
df_transposed.columns.name = None

# --- Code cell 213 ---
# df_transposed.head()
__auto_show__(df_transposed.head())

# --- Code cell 214 ---
df_New = df_transposed.T

# --- Code cell 215 ---
df_New.insert(1, '1997', np.nan)
df_New.insert(3, '1999', np.nan)
# df_New.insert(5, '2001', np.nan)
__auto_show__(df_New.insert(5, '2001', np.nan))

# --- Code cell 216 ---
missing_data = pd.DataFrame(index = df.index, columns = ['1994', '1995'])

df_New = pd.concat([missing_data, df_New], axis = 1)

df_New = df_New.sort_index()

# print(df_New)
__auto_show__(print(df_New))

# --- Code cell 217 ---
# df_New.head()
__auto_show__(df_New.head())

# --- Code cell 218 ---
df14 = df_New.T

# --- Code cell 219 ---
# df14.head()
__auto_show__(df14.head())

# --- Code cell 220 ---
df14.index.name = 'Year'

# --- Code cell 221 ---
df14 = df14[['United States','United Kingdom','Japan','China']]

# --- Code cell 222 ---
# df14.isnull().sum()
__auto_show__(df14.isnull().sum())

# --- Code cell 223 ---
def fill_missing_values(df14, column):
    df14.index = df14.index.astype(int)
    First_Year = df14[column].first_valid_index()
    Last_Year = df14[column].last_valid_index()

    trend = (df14.loc[Last_Year, column] - df14.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df14[df14[column].isnull()].index
    df14.loc[missing_years, column] = df14.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df14, 'China')
fill_missing_values(df14, 'Japan')
fill_missing_values(df14, 'United States')
fill_missing_values(df14, 'United Kingdom')

# print(df14)
__auto_show__(print(df14))

# --- Code cell 224 ---
# df14.isnull().sum()
__auto_show__(df14.isnull().sum())

# --- Code cell 225 ---
df14['United States'] = df14['United States'].astype(float)
df14['United Kingdom'] = df14['United Kingdom'].astype(float)
df14['Japan'] = df14['Japan'].astype(float)
df14['China'] = df14['China'].astype(float)

# --- Code cell 226 ---
# df14.describe()
__auto_show__(df14.describe())

# --- Markdown cell 227 ---
# # Life Expectancy At Birth

# --- Code cell 228 ---
df=pd.read_excel("/work/Life Expectancy at Birth.xlsx")

# --- Code cell 229 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 230 ---
df15 = df.rename(columns={'Unnamed: 0':'Year'})

# --- Code cell 231 ---
# df15.head()
__auto_show__(df15.head())

# --- Code cell 232 ---
# df15.isnull().sum()
__auto_show__(df15.isnull().sum())

# --- Code cell 233 ---
# df15.set_index('Year',inplace=True)
__auto_show__(df15.set_index('Year',inplace=True))

# --- Code cell 234 ---
# df15.head()
__auto_show__(df15.head())

# --- Code cell 235 ---
def fill_missing_values(df15, column):
    df15.index = df15.index.astype(int)
    First_Year = df15[column].first_valid_index()
    Last_Year = df15[column].last_valid_index()

    trend = (df15.loc[Last_Year, column] - df15.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df15[df15[column].isnull()].index
    df15.loc[missing_years, column] = df15.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df15, 'Japan')
fill_missing_values(df15, 'United Kingdom')
fill_missing_values(df15, 'United States')

# print(df15)
__auto_show__(print(df15))

# --- Code cell 236 ---
# df15.describe()
__auto_show__(df15.describe())

# --- Code cell 237 ---
# df15.tail()
__auto_show__(df15.tail())

# --- Markdown cell 238 ---
# # Tourism

# --- Code cell 239 ---
df = pd.read_excel("/work/Tourism Data.xlsx",sheet_name = 'Tourist Arrivals')

# --- Code cell 240 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 241 ---
df = df.rename(columns={'Unnamed: 0':'Country'})

# --- Code cell 242 ---
# df.set_index('Country', inplace = True)
__auto_show__(df.set_index('Country', inplace = True))

# --- Code cell 243 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 244 ---
df16=df.T

# --- Code cell 245 ---
# df16.head()
__auto_show__(df16.head())

# --- Code cell 246 ---
df16.index.name = 'Year'

# --- Code cell 247 ---
# df16.head()
__auto_show__(df16.head())

# --- Code cell 248 ---
df16['United States'] = df16['United States'].replace('..', np.nan)

# --- Code cell 249 ---
# df16.isnull().sum()
__auto_show__(df16.isnull().sum())

# --- Code cell 250 ---
def fill_missing_values(df16, column):
    df16.index = df16.index.astype(int)
    First_Year = df16[column].first_valid_index()
    Last_Year = df16[column].last_valid_index()

    trend = (df16.loc[Last_Year, column] - df16.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df16[df16[column].isnull()].index
    df16.loc[missing_years, column] = df16.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df16, 'China')
fill_missing_values(df16, 'Japan')
fill_missing_values(df16, 'United States')
fill_missing_values(df16, 'United Kingdom')

# print(df16)
__auto_show__(print(df16))

# --- Code cell 251 ---
# df16.isnull().sum()
__auto_show__(df16.isnull().sum())

# --- Code cell 252 ---
# df16.head()
__auto_show__(df16.head())

# --- Code cell 253 ---
df16['United States'] = df16['United States'].astype(float)
df16['United Kingdom'] = df16['United Kingdom'].astype(float)
df16['Japan'] = df16['Japan'].astype(float)
df16['China'] = df16['China'].astype(float)

# --- Code cell 254 ---
# df16.describe()
__auto_show__(df16.describe())

# --- Markdown cell 255 ---
# # Voice and Accountability

# --- Code cell 256 ---
df = pd.read_excel("/work/wgidataset Final.xlsx", sheet_name = 'VoiceandAccountability')

# --- Code cell 257 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 258 ---
df = df.rename(columns={'Unnamed: 0':'Country'})

# --- Code cell 259 ---
# df.head()
__auto_show__(df.head())

# --- Code cell 260 ---
df.set_index("Country", inplace = True)
# df.head()
__auto_show__(df.head())

# --- Code cell 261 ---
df_transposed = df.T

# --- Code cell 262 ---
df_transposed.index.name = 'Year'

# --- Code cell 263 ---
df_transposed.columns.name = None

# --- Code cell 264 ---
df_New = df_transposed.T

# --- Code cell 265 ---
df_New.insert(1, '1997', np.nan)
df_New.insert(3, '1999', np.nan)
# df_New.insert(5, '2001', np.nan)
__auto_show__(df_New.insert(5, '2001', np.nan))

# --- Code cell 266 ---
missing_data = pd.DataFrame(index = df.index, columns = ['1994', '1995'])

df_New = pd.concat([missing_data, df_New], axis = 1)

df_New = df_New.sort_index()

# print(df_New)
__auto_show__(print(df_New))

# --- Code cell 267 ---
df17 = df_New.T

# --- Code cell 268 ---
# df17.head()
__auto_show__(df17.head())

# --- Code cell 269 ---
df17.index.name = 'Year'

# --- Code cell 270 ---
df17 = df17[['United States','United Kingdom','Japan','China']]

# --- Code cell 271 ---
# df17.head()
__auto_show__(df17.head())

# --- Code cell 272 ---
# df17.isnull().sum()
__auto_show__(df17.isnull().sum())

# --- Code cell 273 ---
def fill_missing_values(df17, column):
    df17.index = df17.index.astype(int)
    First_Year = df17[column].first_valid_index()
    Last_Year = df17[column].last_valid_index()

    trend = (df17.loc[Last_Year, column] - df17.loc[First_Year, column]) / (Last_Year - First_Year)

    missing_years = df17[df17[column].isnull()].index
    df17.loc[missing_years, column] = df17.loc[First_Year, column] + trend * (missing_years - First_Year)

fill_missing_values(df17, 'China')
fill_missing_values(df17, 'Japan')
fill_missing_values(df17, 'United States')
fill_missing_values(df17, 'United Kingdom')

# print(df17)
__auto_show__(print(df17))

# --- Code cell 274 ---
# df17.isnull().sum()
__auto_show__(df17.isnull().sum())

# --- Code cell 275 ---
# df17.head()
__auto_show__(df17.head())

# --- Code cell 276 ---
df17['United States'] = df17['United States'].astype(float)
df17['United Kingdom'] = df17['United Kingdom'].astype(float)
df17['Japan'] = df17['Japan'].astype(float)
df17['China'] = df17['China'].astype(float)

# --- Code cell 277 ---
# df17.describe()
__auto_show__(df17.describe())

# --- Markdown cell 278 ---
# # Column Renaming

# --- Code cell 279 ---
# df1.rename(columns={'United States':'CPI_USA','United Kingdom':'CPI_UK','Japan':'CPI_JAPAN','China':'CPI_CHINA'}, inplace = True)
__auto_show__(df1.rename(columns={'United States':'CPI_USA','United Kingdom':'CPI_UK','Japan':'CPI_JAPAN','China':'CPI_CHINA'}, inplace = True))

# --- Code cell 280 ---
# df1.head()
__auto_show__(df1.head())

# --- Code cell 281 ---
# df2.rename(columns = {'United States':'Imports_USA','United Kingdom':'Imports_UK','Japan':'Imports_JAPAN','China':'Imports_CHINA'}, inplace = True)
__auto_show__(df2.rename(columns = {'United States':'Imports_USA','United Kingdom':'Imports_UK','Japan':'Imports_JAPAN','China':'Imports_CHINA'}, inplace = True))

# --- Code cell 282 ---
# df2.head()
__auto_show__(df2.head())

# --- Code cell 283 ---
# df3.rename(columns = {'United States':'Exports_USA','United Kingdom':'Exports_UK','Japan':'Exports_JAPAN','China':'Exports_CHINA'}, inplace = True)
__auto_show__(df3.rename(columns = {'United States':'Exports_USA','United Kingdom':'Exports_UK','Japan':'Exports_JAPAN','China':'Exports_CHINA'}, inplace = True))

# --- Code cell 284 ---
# df3.head()
__auto_show__(df3.head())

# --- Code cell 285 ---
df4.rename(columns = {'United States':'Health_USA','United Kingdom':'Health_UK','Japan':'Health_JAPAN','China':'Health_CHINA'}, inplace = True)
df5.rename(columns = {'United States':'UNEMP_USA','United Kingdom':'UNEMP_UK','Japan':'UNEMP_JAPAN','China':'UNEMP_CHINA'}, inplace = True)
df6.rename(columns = {'United States':'GDP_USA','United Kingdom':'GDP_UK','Japan':'GDP_JAPAN','China':'GDP_CHINA'}, inplace = True)
df7.rename(columns = {'United States':'Manufacturing_USA','United Kingdom':'Manufacturing_UK','Japan':'Manufacturing_JAPAN','China':'Manufacturing_CHINA'}, inplace = True)
df8.rename(columns = {'United States':'ViolenceRate_USA','United Kingdom':'ViolenceRate_UK','Japan':'ViolenceRate_JAPAN','China':'ViolenceRate_CHINA'}, inplace = True)
df9.rename(columns = {'United States':'FDI_USA','United Kingdom':'FDI_UK','Japan':'FDI_JAPAN','China':'FDI_CHINA'}, inplace = True)
df10.rename(columns = {'United States':'GovtExp_USA','United Kingdom':'GovtExp_UK','Japan':'GovtExp_JAPAN','China':'GovtExp_CHINA'}, inplace = True)
df11.rename(columns = {'United States':'ExchRate_USA','United Kingdom':'ExchRate_UK','Japan':'ExchRate_JAPAN','China':'ExchRate_CHINA'}, inplace = True)
df12.rename(columns = {'United States':'RegQuality_USA','United Kingdom':'RegQuality_UK','Japan':'RegQuality_JAPAN','China':'RegQuality_CHINA'}, inplace = True)
df13.rename(columns = {'United States':'Corruption_USA','United Kingdom':'Corruption_UK','Japan':'Corruption_JAPAN','China':'Corruption_CHINA'}, inplace = True)
df14.rename(columns = {'United States':'GovtEff_USA','United Kingdom':'GovtEff_UK','Japan':'GovtEff_JAPAN','China':'GovtEff_CHINA'}, inplace = True)
df15.rename(columns = {'United States':'LifeExp_USA','United Kingdom':'LifeExp_UK','Japan':'LifeExp_JAPAN','China':'LifeExp_CHINA'}, inplace = True)
df16.rename(columns = {'United States':'Tourism_USA','United Kingdom':'Tourism_UK','Japan':'Tourism_JAPAN','China':'Tourism_CHINA'}, inplace = True)
# df17.rename(columns = {'United States':'VoiceAcc_USA','United Kingdom':'VoiceAcc_UK','Japan':'VoiceAcc_JAPAN','China':'VoiceAcc_CHINA'}, inplace = True)
__auto_show__(df17.rename(columns = {'United States':'VoiceAcc_USA','United Kingdom':'VoiceAcc_UK','Japan':'VoiceAcc_JAPAN','China':'VoiceAcc_CHINA'}, inplace = True))

# --- Code cell 287 ---
# df4.head()
__auto_show__(df4.head())

# --- Code cell 288 ---
# df5.head()
__auto_show__(df5.head())

# --- Code cell 289 ---
# df6.head()
__auto_show__(df6.head())

# --- Code cell 290 ---
# df7.head()
__auto_show__(df7.head())

# --- Code cell 291 ---
# df8.head()
__auto_show__(df8.head())

# --- Code cell 292 ---
# df9.head()
__auto_show__(df9.head())

# --- Code cell 293 ---
# df10.head()
__auto_show__(df10.head())

# --- Code cell 294 ---
# df11.head()
__auto_show__(df11.head())

# --- Code cell 295 ---
# df12.head()
__auto_show__(df12.head())

# --- Code cell 296 ---
# df13.head()
__auto_show__(df13.head())

# --- Code cell 297 ---
# df14.head()
__auto_show__(df14.head())

# --- Code cell 298 ---
# df15.head()
__auto_show__(df15.head())

# --- Code cell 299 ---
# df16.head()
__auto_show__(df16.head())

# --- Code cell 300 ---
# df17.head()
__auto_show__(df17.head())

# --- Code cell 301 ---
dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17]

# --- Code cell 302 ---
merged_df = pd.concat(dfs, axis=1)

# --- Code cell 303 ---
# merged_df.head()
__auto_show__(merged_df.head())

# --- Code cell 304 ---
# merged_df.tail()
__auto_show__(merged_df.tail())

# --- Code cell 305 ---
# merged_df.isnull().sum()
__auto_show__(merged_df.isnull().sum())

# --- Code cell 306 ---
# merged_df.columns
__auto_show__(merged_df.columns)

# --- Code cell 307 ---
df_USA = merged_df[['CPI_USA', 'Imports_USA', 'Exports_USA', 'Health_USA', 'UNEMP_USA', 'GDP_USA', 
                    'Manufacturing_USA', 'ViolenceRate_USA', 'FDI_USA', 'GovtExp_USA', 'ExchRate_USA',
                    'RegQuality_USA', 'Corruption_USA', 'GovtEff_USA', 'LifeExp_USA', 'Tourism_USA',
                    'VoiceAcc_USA']]

# --- Code cell 308 ---
# df_USA
__auto_show__(df_USA)

# --- Code cell 309 ---
df_UK = merged_df[['CPI_UK', 'Imports_UK', 'Exports_UK', 'Health_UK', 'UNEMP_UK', 'GDP_UK', 
                    'Manufacturing_UK', 'ViolenceRate_UK', 'FDI_UK', 'GovtExp_UK', 'ExchRate_UK',
                    'RegQuality_UK', 'Corruption_UK', 'GovtEff_UK', 'LifeExp_UK', 'Tourism_UK',
                    'VoiceAcc_UK']]

# --- Code cell 310 ---
# df_UK
__auto_show__(df_UK)

# --- Code cell 311 ---
df_Japan = merged_df[['CPI_JAPAN', 'Imports_JAPAN', 'Exports_JAPAN', 'Health_JAPAN', 'UNEMP_JAPAN', 'GDP_JAPAN', 
                    'Manufacturing_JAPAN', 'ViolenceRate_JAPAN', 'FDI_JAPAN', 'GovtExp_JAPAN', 'ExchRate_JAPAN',
                    'RegQuality_JAPAN', 'Corruption_JAPAN', 'GovtEff_JAPAN', 'LifeExp_JAPAN', 'Tourism_JAPAN',
                    'VoiceAcc_JAPAN']]

# --- Code cell 312 ---
# df_Japan
__auto_show__(df_Japan)

# --- Code cell 313 ---
df_China = merged_df[['CPI_CHINA', 'Imports_CHINA', 'Exports_CHINA', 'Health_CHINA', 'UNEMP_CHINA', 'GDP_CHINA', 
                    'Manufacturing_CHINA', 'ViolenceRate_CHINA', 'FDI_CHINA', 'GovtExp_CHINA', 'ExchRate_CHINA',
                    'RegQuality_CHINA', 'Corruption_CHINA', 'GovtEff_CHINA', 'LifeExp_CHINA', 'Tourism_CHINA',
                    'VoiceAcc_CHINA']]

# --- Code cell 314 ---
# df_China
__auto_show__(df_China)

# --- Markdown cell 315 ---
# # Heatmap

# --- Code cell 316 ---
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(df_USA.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (USA)')
# plt.show()
__auto_show__(plt.show())

# --- Code cell 317 ---
plt.figure(figsize=(10, 8))
sns.heatmap(df_UK.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (UK)')
# plt.show()
__auto_show__(plt.show())

# --- Code cell 318 ---
plt.figure(figsize=(10, 8))
sns.heatmap(df_China.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (China)')
# plt.show()
__auto_show__(plt.show())

# --- Code cell 319 ---
plt.figure(figsize=(10, 8))
sns.heatmap(df_Japan.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (Japan)')
# plt.show()
__auto_show__(plt.show())

# --- Code cell 320 ---
# Converting the index to integer
df_USA.index = df_USA.index.astype(int)
df_UK.index = df_UK.index.astype(int)
df_China.index = df_China.index.astype(int) 
df_Japan.index = df_Japan.index.astype(int)

# --- Markdown cell 321 ---
# # Line Charts

# --- Code cell 322 ---
for column in df_USA.columns:
    plt.figure(figsize=(6, 6))
    plt.plot(df_USA.index, df_USA[column])
    plt.xlabel('Year')
    plt.ylabel(column)
    plt.tight_layout()
    plt.title(f'Line Chart of {column} (USA)')
    plt.show()

# --- Code cell 323 ---
for column in df_UK.columns:
    plt.figure(figsize=(6, 6))
    plt.plot(df_UK.index, df_UK[column])
    plt.xlabel('Year')
    plt.ylabel(column)
    plt.tight_layout()
    plt.title(f'Line Chart of {column} (UK)')
    plt.show()

# --- Code cell 324 ---
for column in df_China.columns:
    plt.figure(figsize=(6, 6))
    plt.plot(df_China.index, df_China[column])
    plt.xlabel('Year')
    plt.ylabel(column)
    plt.tight_layout()
    plt.title(f'Line Chart of {column} (China)')
    plt.show()

# --- Code cell 325 ---
for column in df_Japan.columns:
    plt.figure(figsize=(6, 6))
    plt.plot(df_Japan.index, df_Japan[column])
    plt.xlabel('Year')
    plt.ylabel(column)
    plt.tight_layout()
    plt.title(f'Line Chart of {column} (JAPAN)')
    plt.show()

# --- Code cell 326 ---
# df_USA
__auto_show__(df_USA)

# --- Code cell 327 ---
# List of dataframes
dataframes = [df_USA, df_UK, df_Japan, df_China]

# Iterate through each dataframe and print column names
for i, df in enumerate(dataframes, 1):
    print(f"Columns for df_{i}:")
    print(df.columns.tolist())
    print()

# --- Code cell 328 ---
# Remove 'CPI' and 'ExchRate' columns from df_1
df_USA.drop(columns=['CPI_USA', 'ExchRate_USA'], inplace=True)

# Remove 'CPI' and 'ExchRate' columns from df_2
df_UK.drop(columns=['CPI_UK', 'ExchRate_UK'], inplace=True)

# Remove 'CPI' and 'ExchRate' columns from df_3
df_Japan.drop(columns=['CPI_JAPAN', 'ExchRate_JAPAN'], inplace=True)

# Remove 'CPI' and 'ExchRate' columns from df_4
# df_China.drop(columns=['CPI_CHINA', 'ExchRate_CHINA'], inplace=True)
__auto_show__(df_China.drop(columns=['CPI_CHINA', 'ExchRate_CHINA'], inplace=True))

# --- Code cell 329 ---
# df_USA
__auto_show__(df_USA)

# --- Code cell 330 ---
# Create a new column by subtracting 'Imports' from 'Exports'
df_USA['Trade_Balance_USA'] = df_USA['Exports_USA'] - df_USA['Imports_USA']

df_UK['Trade_Balance_UK'] = df_UK['Exports_UK'] - df_UK['Imports_UK']


df_Japan['Trade_Balance_JAPAN'] = df_Japan['Exports_JAPAN'] - df_Japan['Imports_JAPAN']


df_China['Trade_Balance_CHINA'] = df_China['Exports_CHINA'] - df_China['Imports_CHINA']


# --- Code cell 331 ---
df_USA.drop(columns=['Imports_USA', 'Exports_USA'], inplace=True)
df_UK.drop(columns=['Imports_UK', 'Exports_UK'], inplace=True)
df_Japan.drop(columns=['Imports_JAPAN', 'Exports_JAPAN'], inplace=True)
# df_China.drop(columns=['Imports_CHINA', 'Exports_CHINA'], inplace=True)
__auto_show__(df_China.drop(columns=['Imports_CHINA', 'Exports_CHINA'], inplace=True))

# --- Code cell 332 ---
# df_USA.head()
__auto_show__(df_USA.head())

# --- Code cell 333 ---
# df_USA
__auto_show__(df_USA)

# --- Code cell 334 ---
# Move GDP column to the last position
gdp_column = df_USA.pop('GDP_USA')
df_USA['GDP_USA'] = gdp_column

# Now the GDP column should be the last column in your DataFrame

# --- Code cell 335 ---
# df_USA
__auto_show__(df_USA)

# --- Code cell 336 ---
# df_USA.columns
__auto_show__(df_USA.columns)

# --- Code cell 337 ---
# len(df_USA)
__auto_show__(len(df_USA))

# --- Code cell 338 ---
# print(df_USA.index)
__auto_show__(print(df_USA.index))

# --- Code cell 339 ---
# df_USA
__auto_show__(df_USA)

# --- Code cell 340 ---
# print(df_USA.index)
__auto_show__(print(df_USA.index))

# --- Code cell 341 ---
# df_USA
__auto_show__(df_USA)

# --- Markdown cell 342 ---
# # ARIMA Model (USA)

# --- Code cell 343 ---
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Selecting all features including GDP_USA
X = df_USA.iloc[:, :-1]  # Excluding the last column
y = df_USA.iloc[:, -1]    # Selecting only the last column (GDP_USA)

# Apply differencing to make the data stationary
y_diff = y.diff().dropna()

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Define the window size
window_size = 20

# Iterate over the years starting from 2020
for year in range(2020, 2023):
    # Determine the training data range
    train_start = year - window_size
    train_end = min(2019, year - 1)

    # Determine the test data range
    test_year = year

    # Split the dataset into training and test sets
    X_train = X.loc[train_start:train_end]
    y_train_diff = y_diff.loc[train_start:train_end]
    X_test = X.loc[test_year:test_year]

    # Train the ARIMA model
    try:
        model = ARIMA(y_train_diff, order=(20,1,0)) 
        model_fit = model.fit()

        # Forecast GDP difference for the next year
        forecast_diff = model_fit.forecast(steps=1) # Forecast for 1 year

        # Convert the forecasted difference back to the original scale
        forecast = forecast_diff + y.iloc[-1] 

        # Append forecasted GDP to the list
        forecast_values.append(forecast)

        # Extract actual GDP value for the next year from the DataFrame
        actual_gdp_value = df_USA.loc[test_year, 'GDP_USA']
        actual_gdp_values.append(actual_gdp_value)

        # Print the forecasted GDP for the next year
        print("Forecasted GDP for", test_year, ":", forecast)

        # Remove the test value from the training set for the next iteration
        X = X.drop(index=test_year)
        y = y.drop(index=test_year)
    except Exception as e:
        print(f"Failed to forecast GDP for {test_year}: {str(e)}")

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Markdown cell 344 ---
# # LSTM Model (USA)

# --- Code cell 345 ---
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import numpy as np

# Convert the dataframe to numpy arrays
X = df_USA.iloc[:, :-1].values
y = df_USA.iloc[:, -1].values

# Apply Min-Max scaling to the data
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.reshape(-1, 1))

# Define the window size
window_size = 20

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Get the DataFrame index as years
years = df_USA.index.values

# Iterate over the years starting from 2020
for i in range(len(years)):
    if years[i] < 2020:  # Skip years before 2020
        continue
    
    # Determine the training data range (excluding the previous test year)
    train_start = max(0, i - window_size)
    train_end = i - 1
    if train_end >= 2020:  # Exclude the test year from the previous iteration
        train_end = min(2019, i - 1)

    # Determine the test data range
    test_year = years[i]

    # Split the dataset into training and test sets
    X_train = X_scaled[train_start:train_end+1]
    y_train = y_scaled[train_start:train_end+1]
    X_test = X_scaled[i:i+1]  # Selecting a single year as test data

    # Reshape the data for LSTM
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1]))

    # Reshape the data for LSTM (2D)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Define the LSTM model
    model = Sequential()
    model.add(LSTM(units=100, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the LSTM model
    model.fit(X_train, y_train, epochs=300, batch_size=64, verbose=0)

    # Forecast GDP for the next year
    forecast_scaled = model.predict(X_test)
    forecast = scaler.inverse_transform(forecast_scaled)

    # Append forecasted GDP to the list
    forecast_values.append(forecast)

    # Extract actual GDP value for the next year from the DataFrame
    actual_gdp_value = df_USA.loc[test_year, 'GDP_USA']
    actual_gdp_values.append(actual_gdp_value)

    # Print the forecasted GDP for the next year
    print("Forecasted GDP for", test_year, ":", forecast)

# Convert forecast_values and actual_gdp_values to numpy arrays
forecast_values = np.array(forecast_values).reshape(-1)
actual_gdp_values = np.array(actual_gdp_values)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Code cell 346 ---
# df_UK
__auto_show__(df_UK)

# --- Code cell 347 ---
# Move GDP column to the last position
gdp_column = df_UK.pop('GDP_UK')
df_UK['GDP_UK'] = gdp_column

# --- Code cell 348 ---
# df_UK
__auto_show__(df_UK)

# --- Markdown cell 349 ---
# # ARIMA (UK)

# --- Code cell 350 ---
# Selecting all features including GDP_UK
X = df_UK.iloc[:, :-1]  # Excluding the last column
y = df_UK.iloc[:, -1]    # Selecting only the last column (GDP_UK)

# Apply differencing to make the data stationary
y_diff = y.diff().dropna()

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Define the window size
window_size = 20

# Iterate over the years starting from 2020
for year in range(2020, 2023):
    # Determine the training data range
    train_start = year - window_size
    train_end = min(2019, year - 1)

    # Determine the test data range
    test_year = year

    # Split the dataset into training and test sets
    X_train = X.loc[train_start:train_end]
    y_train_diff = y_diff.loc[train_start:train_end]
    X_test = X.loc[test_year:test_year]

    # Train the ARIMA model
    try:
        model = ARIMA(y_train_diff, order=(20,1,0)) 
        model_fit = model.fit()

        # Forecast GDP difference for the next year
        forecast_diff = model_fit.forecast(steps=1) # Forecast for 1 year

        # Convert the forecasted difference back to the original scale
        forecast = forecast_diff + y.iloc[-1] 

        # Append forecasted GDP to the list
        forecast_values.append(forecast)

        # Extract actual GDP value for the next year from the DataFrame
        actual_gdp_value = df_UK.loc[test_year, 'GDP_UK']
        actual_gdp_values.append(actual_gdp_value)

        # Print the forecasted GDP for the next year
        print("Forecasted GDP for", test_year, ":", forecast)

        # Remove the test value from the training set for the next iteration
        X = X.drop(index=test_year)
        y = y.drop(index=test_year)
    except Exception as e:
        print(f"Failed to forecast GDP for {test_year}: {str(e)}")

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Markdown cell 351 ---
# # LSTM Model (UK)

# --- Code cell 352 ---
# Convert the dataframe to numpy arrays
X = df_UK.iloc[:, :-1].values
y = df_UK.iloc[:, -1].values

# Apply Min-Max scaling to the data
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.reshape(-1, 1))

# Define the window size
window_size = 20

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Get the DataFrame index as years
years = df_UK.index.values

# Iterate over the years starting from 2020
for i in range(len(years)):
    if years[i] < 2020:  # Skip years before 2020
        continue
    
    # Determine the training data range (excluding the previous test year)
    train_start = max(0, i - window_size)
    train_end = i - 1
    if train_end >= 2020:  # Exclude the test year from the previous iteration
        train_end = min(2019, i - 1)

    # Determine the test data range
    test_year = years[i]

    # Split the dataset into training and test sets
    X_train = X_scaled[train_start:train_end+1]
    y_train = y_scaled[train_start:train_end+1]
    X_test = X_scaled[i:i+1]  # Selecting a single year as test data

    # Reshape the data for LSTM
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1]))

    # Reshape the data for LSTM (2D)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Define the LSTM model
    model = Sequential()
    model.add(LSTM(units=100, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the LSTM model
    model.fit(X_train, y_train, epochs=300, batch_size=64, verbose=0)

    # Forecast GDP for the next year
    forecast_scaled = model.predict(X_test)
    forecast = scaler.inverse_transform(forecast_scaled)

    # Append forecasted GDP to the list
    forecast_values.append(forecast)

    # Extract actual GDP value for the next year from the DataFrame
    actual_gdp_value = df_UK.loc[test_year, 'GDP_UK']
    actual_gdp_values.append(actual_gdp_value)

    # Print the forecasted GDP for the next year
    print("Forecasted GDP for", test_year, ":", forecast)

# Convert forecast_values and actual_gdp_values to numpy arrays
forecast_values = np.array(forecast_values).reshape(-1)
actual_gdp_values = np.array(actual_gdp_values)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Code cell 353 ---
# df_China
__auto_show__(df_China)

# --- Code cell 354 ---
# Move GDP column to the last position
gdp_column = df_China.pop('GDP_CHINA')
df_China['GDP_CHINA'] = gdp_column

# --- Code cell 355 ---
# df_China
__auto_show__(df_China)

# --- Markdown cell 356 ---
# # ARIMA (China)

# --- Code cell 357 ---
# Selecting all features including GDP_CHINA
X = df_China.iloc[:, :-1]  # Excluding the last column
y = df_China.iloc[:, -1]    # Selecting only the last column (GDP_CHINA)

# Apply differencing to make the data stationary
y_diff = y.diff().dropna()

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Define the window size
window_size = 20

# Iterate over the years starting from 2020
for year in range(2020, 2023):
    # Determine the training data range
    train_start = year - window_size
    train_end = min(2019, year - 1)

    # Determine the test data range
    test_year = year

    # Split the dataset into training and test sets
    X_train = X.loc[train_start:train_end]
    y_train_diff = y_diff.loc[train_start:train_end]
    X_test = X.loc[test_year:test_year]

    # Train the ARIMA model
    try:
        model = ARIMA(y_train_diff, order=(20,1,0)) 
        model_fit = model.fit()

        # Forecast GDP difference for the next year
        forecast_diff = model_fit.forecast(steps=1) # Forecast for 1 year

        # Convert the forecasted difference back to the original scale
        forecast = forecast_diff + y.iloc[-1] 

        # Append forecasted GDP to the list
        forecast_values.append(forecast)

        # Extract actual GDP value for the next year from the DataFrame
        actual_gdp_value = df_China.loc[test_year, 'GDP_CHINA']
        actual_gdp_values.append(actual_gdp_value)

        # Print the forecasted GDP for the next year
        print("Forecasted GDP for", test_year, ":", forecast)

        # Remove the test value from the training set for the next iteration
        X = X.drop(index=test_year)
        y = y.drop(index=test_year)
    except Exception as e:
        print(f"Failed to forecast GDP for {test_year}: {str(e)}")

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Markdown cell 358 ---
# # LSTM Model (China)

# --- Code cell 359 ---
# Convert the dataframe to numpy arrays
X = df_China.iloc[:, :-1].values
y = df_China.iloc[:, -1].values

# Apply Min-Max scaling to the data
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.reshape(-1, 1))

# Define the window size
window_size = 20

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Get the DataFrame index as years
years = df_China.index.values

# Iterate over the years starting from 2020
for i in range(len(years)):
    if years[i] < 2020:  # Skip years before 2020
        continue
    
    # Determine the training data range (excluding the previous test year)
    train_start = max(0, i - window_size)
    train_end = i - 1
    if train_end >= 2020:  # Exclude the test year from the previous iteration
        train_end = min(2019, i - 1)

    # Determine the test data range
    test_year = years[i]

    # Split the dataset into training and test sets
    X_train = X_scaled[train_start:train_end+1]
    y_train = y_scaled[train_start:train_end+1]
    X_test = X_scaled[i:i+1]  # Selecting a single year as test data

    # Reshape the data for LSTM
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1]))

    # Reshape the data for LSTM (2D)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Define the LSTM model
    model = Sequential()
    model.add(LSTM(units=100, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the LSTM model
    model.fit(X_train, y_train, epochs=300, batch_size=64, verbose=0)

    # Forecast GDP for the next year
    forecast_scaled = model.predict(X_test)
    forecast = scaler.inverse_transform(forecast_scaled)

    # Append forecasted GDP to the list
    forecast_values.append(forecast)

    # Extract actual GDP value for the next year from the DataFrame
    actual_gdp_value = df_China.loc[test_year, 'GDP_CHINA']
    actual_gdp_values.append(actual_gdp_value)

    # Print the forecasted GDP for the next year
    print("Forecasted GDP for", test_year, ":", forecast)

# Convert forecast_values and actual_gdp_values to numpy arrays
forecast_values = np.array(forecast_values).reshape(-1)
actual_gdp_values = np.array(actual_gdp_values)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Code cell 360 ---
# Move GDP column to the last position
gdp_column = df_Japan.pop('GDP_JAPAN')
df_Japan['GDP_JAPAN'] = gdp_column

# --- Code cell 361 ---
# df_Japan
__auto_show__(df_Japan)

# --- Markdown cell 362 ---
# # ARIMA (Japan)

# --- Code cell 363 ---
# Selecting all features including GDP_JAPAN
X = df_Japan.iloc[:, :-1]  # Excluding the last column
y = df_Japan.iloc[:, -1]    # Selecting only the last column (GDP_JAPAN)

# Apply differencing to make the data stationary
y_diff = y.diff().dropna()

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Define the window size
window_size = 20

# Iterate over the years starting from 2020
for year in range(2020, 2023):
    # Determine the training data range
    train_start = year - window_size
    train_end = min(2019, year - 1)

    # Determine the test data range
    test_year = year

    # Split the dataset into training and test sets
    X_train = X.loc[train_start:train_end]
    y_train_diff = y_diff.loc[train_start:train_end]
    X_test = X.loc[test_year:test_year]

    # Train the ARIMA model
    try:
        model = ARIMA(y_train_diff, order=(20,1,0)) 
        model_fit = model.fit()

        # Forecast GDP difference for the next year
        forecast_diff = model_fit.forecast(steps=1) # Forecast for 1 year

        # Convert the forecasted difference back to the original scale
        forecast = forecast_diff + y.iloc[-1] 

        # Append forecasted GDP to the list
        forecast_values.append(forecast)

        # Extract actual GDP value for the next year from the DataFrame
        actual_gdp_value = df_Japan.loc[test_year, 'GDP_JAPAN']
        actual_gdp_values.append(actual_gdp_value)

        # Print the forecasted GDP for the next year
        print("Forecasted GDP for", test_year, ":", forecast)

        # Remove the test value from the training set for the next iteration
        X = X.drop(index=test_year)
        y = y.drop(index=test_year)
    except Exception as e:
        print(f"Failed to forecast GDP for {test_year}: {str(e)}")

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Markdown cell 364 ---
# # LSTM Model (Japan)

# --- Code cell 365 ---
# Convert the dataframe to numpy arrays
X = df_Japan.iloc[:, :-1].values
y = df_Japan.iloc[:, -1].values

# Apply Min-Max scaling to the data
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.reshape(-1, 1))

# Define the window size
window_size = 20

# Initialize lists to store forecasts and actual GDP values
forecast_values = []
actual_gdp_values = []

# Get the DataFrame index as years
years = df_Japan.index.values

# Iterate over the years starting from 2020
for i in range(len(years)):
    if years[i] < 2020:  # Skip years before 2020
        continue
    
    # Determine the training data range (excluding the previous test year)
    train_start = max(0, i - window_size)
    train_end = i - 1
    if train_end >= 2020:  # Exclude the test year from the previous iteration
        train_end = min(2019, i - 1)

    # Determine the test data range
    test_year = years[i]

    # Split the dataset into training and test sets
    X_train = X_scaled[train_start:train_end+1]
    y_train = y_scaled[train_start:train_end+1]
    X_test = X_scaled[i:i+1]  # Selecting a single year as test data

    # Reshape the data for LSTM
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1]))

    # Reshape the data for LSTM (2D)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Define the LSTM model
    model = Sequential()
    model.add(LSTM(units=100, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the LSTM model
    model.fit(X_train, y_train, epochs=300, batch_size=64, verbose=0)

    # Forecast GDP for the next year
    forecast_scaled = model.predict(X_test)
    forecast = scaler.inverse_transform(forecast_scaled)

    # Append forecasted GDP to the list
    forecast_values.append(forecast)

    # Extract actual GDP value for the next year from the DataFrame
    actual_gdp_value = df_Japan.loc[test_year, 'GDP_JAPAN']
    actual_gdp_values.append(actual_gdp_value)

    # Print the forecasted GDP for the next year
    print("Forecasted GDP for", test_year, ":", forecast)

# Convert forecast_values and actual_gdp_values to numpy arrays
forecast_values = np.array(forecast_values).reshape(-1)
actual_gdp_values = np.array(actual_gdp_values)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_gdp_values, forecast_values))
print("RMSE:", rmse)

# Calculate accuracy (as a percentage)
accuracy = 100 * (1 - (rmse / np.mean(actual_gdp_values)))
# print("Accuracy:", accuracy, "%")
__auto_show__(print("Accuracy:", accuracy, "%"))

# --- Code cell 366 ---
pip install matplotlib numpy scikit-learn

# --- Markdown cell 367 ---
# # Permutation Based Feature Importance

# --- Code cell 368 ---
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.evaluate import feature_importance_permutation
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Assuming you have df_USA with features and target variable
# X should contain the features, and y should contain the target variable

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df_USA.drop(columns=['GDP_USA']),  # Exclude the target variable
    df_USA['GDP_USA'], 
    test_size=0.2, 
    random_state=123
)    

# Instantiate the RandomForestRegressor model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=123)

# Fit the RandomForestRegressor model
rf_regressor.fit(X_train, y_train)

# Calculate feature importance using permutation
imp_vals, _ = feature_importance_permutation(
    predict_method=rf_regressor.predict, 
    X=X_test.values,  # Convert DataFrame to numpy array
    y=y_test.values,  # Convert Series to numpy array
    metric='r2',       # Use the appropriate metric for regression
    num_rounds=5,
    seed=1
)

# Plot the feature importance
plt.figure(figsize=(8, 6))
bars = plt.bar(range(X_test.shape[1]), imp_vals)
plt.xticks(range(X_test.shape[1]), X_test.columns, rotation=90)
plt.xlabel('Features')
plt.ylabel('Permutation Importance')
plt.title('Most Significant Features - USA')

# Set colors for bars
most_important_index = np.argmax(imp_vals)
for idx, bar in enumerate(bars):
    if idx == most_important_index:
        bar.set_color('#117733')  # Paul Tol's R051 Green
    else:
        bar.set_color('#88CCEE')  # Paul Tol's R148 Light blue

plt.tight_layout()
# plt.show()
__auto_show__(plt.show())

# --- Code cell 369 ---
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.evaluate import feature_importance_permutation
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Assuming you have df_USA with features and target variable
# X should contain the features, and y should contain the target variable

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df_China.drop(columns=['GDP_CHINA']),  # Exclude the target variable
    df_China['GDP_CHINA'], 
    test_size=0.2, 
    random_state=123
)    

# Instantiate the RandomForestRegressor model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=123)

# Fit the RandomForestRegressor model
rf_regressor.fit(X_train, y_train)

# Calculate feature importance using permutation
imp_vals, _ = feature_importance_permutation(
    predict_method=rf_regressor.predict, 
    X=X_test.values,  # Convert DataFrame to numpy array
    y=y_test.values,  # Convert Series to numpy array
    metric='r2',       # Use the appropriate metric for regression
    num_rounds=10,
    seed=1
)

# Plot the feature importance
plt.figure(figsize=(8, 6))
bars = plt.bar(range(X_test.shape[1]), imp_vals)
plt.xticks(range(X_test.shape[1]), X_test.columns, rotation=90)
plt.xlabel('Features')
plt.ylabel('Permutation Importance')
plt.title('Most Significant Features - China')

# Set colors for bars
most_important_index = np.argmax(imp_vals)
for idx, bar in enumerate(bars):
    if idx == most_important_index:
        bar.set_color('#117733')  # Paul Tol's R051 Green
    else:
        bar.set_color('#88CCEE')  # Paul Tol's R148 Light blue

plt.tight_layout()
# plt.show()
__auto_show__(plt.show())

# --- Code cell 370 ---
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.evaluate import feature_importance_permutation
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Assuming you have df_USA with features and target variable
# X should contain the features, and y should contain the target variable

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df_UK.drop(columns=['GDP_UK']),  # Exclude the target variable
    df_UK['GDP_UK'], 
    test_size=0.2, 
    random_state=123
)    

# Instantiate the RandomForestRegressor model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=123)

# Fit the RandomForestRegressor model
rf_regressor.fit(X_train, y_train)

# Calculate feature importance using permutation
imp_vals, _ = feature_importance_permutation(
    predict_method=rf_regressor.predict, 
    X=X_test.values,  # Convert DataFrame to numpy array
    y=y_test.values,  # Convert Series to numpy array
    metric='r2',       # Use the appropriate metric for regression
    num_rounds=5,
    seed=1
)

# Plot the feature importance
plt.figure(figsize=(8, 6))
bars = plt.bar(range(X_test.shape[1]), imp_vals)
plt.xticks(range(X_test.shape[1]), X_test.columns, rotation=90)
plt.xlabel('Features')
plt.ylabel('Permutation Importance')
plt.title('Most Significant Features - UK')

# Set colors for bars
most_important_index = np.argmax(imp_vals)
for idx, bar in enumerate(bars):
    if idx == most_important_index:
        bar.set_color('#117733')  # Paul Tol's R051 Green
    else:
        bar.set_color('#88CCEE')  # Paul Tol's R148 Light blue

plt.tight_layout()
# plt.show()
__auto_show__(plt.show())

# --- Code cell 371 ---
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.evaluate import feature_importance_permutation
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Assuming you have df_USA with features and target variable
# X should contain the features, and y should contain the target variable

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df_Japan.drop(columns=['GDP_JAPAN']),  # Exclude the target variable
    df_Japan['GDP_JAPAN'], 
    test_size=0.2, 
    random_state=123
)    

# Instantiate the RandomForestRegressor model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=123)

# Fit the RandomForestRegressor model
rf_regressor.fit(X_train, y_train)

# Calculate feature importance using permutation
imp_vals, _ = feature_importance_permutation(
    predict_method=rf_regressor.predict, 
    X=X_test.values,  # Convert DataFrame to numpy array
    y=y_test.values,  # Convert Series to numpy array
    metric='r2',       # Use the appropriate metric for regression
    num_rounds=5,
    seed=1
)

# Plot the feature importance
plt.figure(figsize=(8, 6))
bars = plt.bar(range(X_test.shape[1]), imp_vals)
plt.xticks(range(X_test.shape[1]), X_test.columns, rotation=90)
plt.xlabel('Features')
plt.ylabel('Permutation Importance')
plt.title('Most Significant Features - Japan')

# Set colors for bars
most_important_index = np.argmax(imp_vals)
for idx, bar in enumerate(bars):
    if idx == most_important_index:
        bar.set_color('#117733')  # Paul Tol's R051 Green
    else:
        bar.set_color('#88CCEE')  # Paul Tol's R148 Light blue

plt.tight_layout()
# plt.show()
__auto_show__(plt.show())

# --- Code cell 372 ---
# df_Japan
__auto_show__(df_Japan)

# --- Code cell 373 ---
# df_USA
__auto_show__(df_USA)

# --- Markdown cell 374 ---
# # PFFRA Analysis

# --- Code cell 375 ---
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from PFFRA import PermFeatureFreqRespoAnalysis  # Assuming you have the PFFRA module

# Assuming df_USA contains the features and target variable
# X should contain the features, and y should contain the target variable

# Selecting the features of interest
selected_features = [ 'Manufacturing_USA', 'Health_USA', 'GovtExp_USA']  # Include GDP_USA as the target variable
X_selected = df_USA[selected_features]
y = df_USA['GDP_USA']  # Target variable is GDP_USA

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Instantiate PFFRA for investigating frequency response
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)

# Investigate multiple features and output their permutation spectrum data
for i in range(X_selected.shape[1]):
    # Instantiate PFFRA for the current feature
    pffra = PermFeatureFreqRespoAnalysis(y=y, X=X_selected, model=model, interested_feature_index=i)
    
    # Generate permutation dataset
    X_interested_feature, X_other_feature = pffra.permuted_dataset(mode='mean')
    
    # Predict target variables using the permutated datasets
    pred_interested_feature, pred_other_feature, pred_all_feature = pffra.permu_pred(X_interested_feature, X_other_feature)
    
    # Calculate the sampling frequency of your time series data
    sampling_frequency = len(y)  # Assuming each data point corresponds to 1 unit of time

    # Calculate the Nyquist frequency (half of the sampling frequency)
    nyquist_frequency = sampling_frequency / 2

    # Define the frequency range based on the Nyquist frequency
    frequency_range = np.linspace(0, nyquist_frequency, num=len(y) // 2)
    
    # Generate spectrums for analysis with the appropriate sample_rate
    spectrums = pffra.gen_spectrum(pred_interested_feature=pred_interested_feature, 
                                    pred_other_feature=pred_other_feature, 
                                    pred_all_feature=pred_all_feature, 
                                    sample_rate=sampling_frequency)
    
    # Unpack spectrums
    spectrum_interested_i = spectrums[0]
    spectrum_all = spectrums[2]
    spectrum_true = spectrums[3]
    frq_range = spectrums[4]
    
    # Plot permuted frequency responses for each component
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 16  
    plt.rcParams["xtick.labelsize"] = "large"
    plt.rcParams["ytick.labelsize"] = "large"
    
    ax1.plot(frq_range[1:], spectrum_interested_i[1:], 
             label="x_{} (DC: {:.2f})".format(i, spectrum_interested_i[0]))
    ax1.legend()
    ax1.set_xlabel("Frequency")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Permuted Frequency Responses for each component")

ax2 = fig.add_subplot(122)
ax2.plot(frq_range[1:], spectrum_all[1:], 
         label="{} (DC: {:.2e})".format("all features", spectrum_all[0]))
ax2.plot(frq_range[1:], spectrum_true[1:], 
         label="{} (DC: {:.2e})".format("True y", spectrum_true[0]))
ax2.legend()
ax2.set_xlim(frq_range[1], frq_range[-1])
ax2.set_xlabel("Frequency ")
ax2.set_ylabel("Magnitude")
ax2.set_title("Frequency Responses for the all components")
# plt.show()
__auto_show__(plt.show())

# --- Code cell 376 ---
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # Import the StandardScaler
from PFFRA import PermFeatureFreqRespoAnalysis  # Assuming you have the PFFRA module

# Assuming df_UK contains the features and target variable
# X should contain the features, and y should contain the target variable

# Selecting the features of interest
selected_features = ['Health_UK', 'GovtExp_UK'] 

X_selected = df_UK[selected_features]
y = df_UK['GDP_UK']  # Target variable is GDP_USA

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Instantiate PFFRA for investigating frequency response
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)

# Investigate multiple features and output their permutation spectrum data
for i in range(X_selected.shape[1]):
    # Instantiate PFFRA for the current feature
    pffra = PermFeatureFreqRespoAnalysis(y=y, X=X_selected, model=model, interested_feature_index=i)
    
    # Generate permutation dataset
    X_interested_feature, X_other_feature = pffra.permuted_dataset(mode='shuffle')
    
    # Predict target variables using the permutated datasets
    pred_interested_feature, pred_other_feature, pred_all_feature = pffra.permu_pred(X_interested_feature, X_other_feature)
    
    sampling_frequency = 1  # Assuming each data point corresponds to 1 unit of time

    # Calculate the Nyquist frequency (half of the sampling frequency)
    nyquist_frequency = sampling_frequency / 2

    # Define the frequency range based on the Nyquist frequency
    frequency_range = np.linspace(0, nyquist_frequency, num=len(y) // 2)
    
    # Generate spectrums for analysis with the appropriate sample_rate
    spectrums = pffra.gen_spectrum(pred_interested_feature=pred_interested_feature, 
                                    pred_other_feature=pred_other_feature, 
                                    pred_all_feature=pred_all_feature, 
                                    sample_rate=sampling_frequency)
    
    # Unpack spectrums
    spectrum_interested_i = spectrums[0]
    spectrum_all = spectrums[2]
    spectrum_true = spectrums[3]
    frq_range = spectrums[4]
    
    # Plot permuted frequency responses for each component
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 16  
    plt.rcParams["xtick.labelsize"] = "large"
    plt.rcParams["ytick.labelsize"] = "large"
    
    ax1.plot(frq_range[1:], spectrum_interested_i[1:], 
             label="{} (DC: {:.2f})".format(selected_features[i], spectrum_interested_i[0]), linewidth = 4)
    ax1.legend(fontsize='large')
    ax1.set_xlabel("Frequency")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Permuted Frequency Responses for each component")

ax2 = fig.add_subplot(122)
ax2.plot(frq_range[1:], spectrum_all[1:], 
         label="{} (DC: {:.2e})".format("all features", spectrum_all[0]), linewidth=4)
ax2.plot(frq_range[1:], spectrum_true[1:], 
         label="{} (DC: {:.2e})".format("True y", spectrum_true[0]), linewidth=4)
ax2.legend(fontsize='large')
ax2.set_xlim(frq_range[1], frq_range[-1])
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")
ax2.set_title("Frequency Responses for the all components")
plt.show()

print(spectrums)
print(spectrums[0])
# print(spectrum_interested_i[0])
__auto_show__(print(spectrum_interested_i[0]))

# --- Code cell 377 ---
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # Import the StandardScaler
from PFFRA import PermFeatureFreqRespoAnalysis  # Assuming you have the PFFRA module

# Assuming df_UK contains the features and target variable
# X should contain the features, and y should contain the target variable

# Selecting the features of interest
selected_features = ['GovtExp_USA', 'Manufacturing_USA'] 

X_selected = df_USA[selected_features]
y = df_USA['GDP_USA']  # Target variable is GDP_USA

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Instantiate PFFRA for investigating frequency response
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)

# Investigate multiple features and output their permutation spectrum data
for i in range(X_selected.shape[1]):
    # Instantiate PFFRA for the current feature
    pffra = PermFeatureFreqRespoAnalysis(y=y, X=X_selected, model=model, interested_feature_index=i)
    
    # Generate permutation dataset
    X_interested_feature, X_other_feature = pffra.permuted_dataset(mode='shuffle')
    
    # Predict target variables using the permutated datasets
    pred_interested_feature, pred_other_feature, pred_all_feature = pffra.permu_pred(X_interested_feature, X_other_feature)
    
    sampling_frequency = 1  # Assuming each data point corresponds to 1 unit of time

    # Calculate the Nyquist frequency (half of the sampling frequency)
    nyquist_frequency = sampling_frequency / 2

    # Define the frequency range based on the Nyquist frequency
    frequency_range = np.linspace(0, nyquist_frequency, num=len(y) // 2)
    
    # Generate spectrums for analysis with the appropriate sample_rate
    spectrums = pffra.gen_spectrum(pred_interested_feature=pred_interested_feature, 
                                    pred_other_feature=pred_other_feature, 
                                    pred_all_feature=pred_all_feature, 
                                    sample_rate=sampling_frequency)
    
    # Unpack spectrums
    spectrum_interested_i = spectrums[0]
    spectrum_all = spectrums[2]
    spectrum_true = spectrums[3]
    frq_range = spectrums[4]
    
    # Plot permuted frequency responses for each component
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 16  
    plt.rcParams["xtick.labelsize"] = "large"
    plt.rcParams["ytick.labelsize"] = "large"
    
    ax1.plot(frq_range[1:], spectrum_interested_i[1:], 
             label="{} (DC: {:.2f})".format(selected_features[i], spectrum_interested_i[0]), linewidth = 4)
    ax1.legend(fontsize='large')
    ax1.set_xlabel("Frequency")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Permuted Frequency Responses for each component")

ax2 = fig.add_subplot(122)
ax2.plot(frq_range[1:], spectrum_all[1:], 
         label="{} (DC: {:.2e})".format("all features", spectrum_all[0]), linewidth=4)
ax2.plot(frq_range[1:], spectrum_true[1:], 
         label="{} (DC: {:.2e})".format("True y", spectrum_true[0]), linewidth=4)
ax2.legend(fontsize='large')
ax2.set_xlim(frq_range[1], frq_range[-1])
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")
ax2.set_title("Frequency Responses for the all components")
# plt.show()
__auto_show__(plt.show())

# --- Code cell 378 ---
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # Import the StandardScaler
from PFFRA import PermFeatureFreqRespoAnalysis  # Assuming you have the PFFRA module

# Assuming df_UK contains the features and target variable
# X should contain the features, and y should contain the target variable

# Selecting the features of interest
selected_features = ['GovtExp_CHINA','LifeExp_CHINA'] 

X_selected = df_China[selected_features]
y = df_China['GDP_CHINA']  # Target variable is GDP_USA

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Instantiate PFFRA for investigating frequency response
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)

# Investigate multiple features and output their permutation spectrum data
for i in range(X_selected.shape[1]):
    # Instantiate PFFRA for the current feature
    pffra = PermFeatureFreqRespoAnalysis(y=y, X=X_selected, model=model, interested_feature_index=i)
    
    # Generate permutation dataset
    X_interested_feature, X_other_feature = pffra.permuted_dataset(mode='shuffle')
    
    # Predict target variables using the permutated datasets
    pred_interested_feature, pred_other_feature, pred_all_feature = pffra.permu_pred(X_interested_feature, X_other_feature)
    
    sampling_frequency = 1  # Assuming each data point corresponds to 1 unit of time

    # Calculate the Nyquist frequency (half of the sampling frequency)
    nyquist_frequency = sampling_frequency / 2

    # Define the frequency range based on the Nyquist frequency
    frequency_range = np.linspace(0, nyquist_frequency, num=len(y) // 2)
    
    # Generate spectrums for analysis with the appropriate sample_rate
    spectrums = pffra.gen_spectrum(pred_interested_feature=pred_interested_feature, 
                                    pred_other_feature=pred_other_feature, 
                                    pred_all_feature=pred_all_feature, 
                                    sample_rate=sampling_frequency)
    
    # Unpack spectrums
    spectrum_interested_i = spectrums[0]
    spectrum_all = spectrums[2]
    spectrum_true = spectrums[3]
    frq_range = spectrums[4]
    
    # Plot permuted frequency responses for each component
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 16  
    plt.rcParams["xtick.labelsize"] = "large"
    plt.rcParams["ytick.labelsize"] = "large"
    
    ax1.plot(frq_range[1:], spectrum_interested_i[1:], 
             label="{} (DC: {:.2f})".format(selected_features[i], spectrum_interested_i[0]), linewidth = 4)
    ax1.legend(fontsize='large')
    ax1.set_xlabel("Frequency")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Permuted Frequency Responses for each component")

ax2 = fig.add_subplot(122)
ax2.plot(frq_range[1:], spectrum_all[1:], 
         label="{} (DC: {:.2e})".format("all features", spectrum_all[0]), linewidth=4)
ax2.plot(frq_range[1:], spectrum_true[1:], 
         label="{} (DC: {:.2e})".format("True y", spectrum_true[0]), linewidth=4)
ax2.legend(fontsize='large')
ax2.set_xlim(frq_range[1], frq_range[-1])
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")
ax2.set_title("Frequency Responses for the all components")
# plt.show()
__auto_show__(plt.show())

# --- Code cell 379 ---
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # Import the StandardScaler
from PFFRA import PermFeatureFreqRespoAnalysis  # Assuming you have the PFFRA module

# Assuming df_UK contains the features and target variable
# X should contain the features, and y should contain the target variable

# Selecting the features of interest
selected_features = ['Manufacturing_JAPAN', 'Trade_Balance_JAPAN'] 

X_selected = df_Japan[selected_features]
y = df_Japan['GDP_JAPAN']  # Target variable is GDP_USA

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Instantiate PFFRA for investigating frequency response
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)

# Investigate multiple features and output their permutation spectrum data
for i in range(X_selected.shape[1]):
    # Instantiate PFFRA for the current feature
    pffra = PermFeatureFreqRespoAnalysis(y=y, X=X_selected, model=model, interested_feature_index=i)
    
    # Generate permutation dataset
    X_interested_feature, X_other_feature = pffra.permuted_dataset(mode='shuffle')
    # Predict target variables using the permutated datasets
    pred_interested_feature, pred_other_feature, pred_all_feature = pffra.permu_pred(X_interested_feature, X_other_feature)
    
    sampling_frequency = 1  # Assuming each data point corresponds to 1 unit of time

    # Calculate the Nyquist frequency (half of the sampling frequency)
    nyquist_frequency = sampling_frequency / 2

    # Define the frequency range based on the Nyquist frequency
    frequency_range = np.linspace(0, nyquist_frequency, num=len(y) // 2)
    
    # Generate spectrums for analysis with the appropriate sample_rate
    spectrums = pffra.gen_spectrum(pred_interested_feature=pred_interested_feature, 
                                    pred_other_feature=pred_other_feature, 
                                    pred_all_feature=pred_all_feature, 
                                    sample_rate=sampling_frequency)
    
    # Unpack spectrums
    spectrum_interested_i = spectrums[0]
    spectrum_all = spectrums[2]
    spectrum_true = spectrums[3]
    frq_range = spectrums[4]
    
    # Plot permuted frequency responses for each component
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 16  
    plt.rcParams["xtick.labelsize"] = "large"
    plt.rcParams["ytick.labelsize"] = "large"
    
    ax1.plot(frq_range[1:], spectrum_interested_i[1:], 
             label="{} (DC: {:.2f})".format(selected_features[i], spectrum_interested_i[0]), linewidth = 4)
    ax1.legend(fontsize='large')
    ax1.set_xlabel("Frequency")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Permuted Frequency Responses for each component")

ax2 = fig.add_subplot(122)
ax2.plot(frq_range[1:], spectrum_all[1:], 
         label="{} (DC: {:.2e})".format("all features", spectrum_all[0]), linewidth=4)
ax2.plot(frq_range[1:], spectrum_true[1:], 
         label="{} (DC: {:.2e})".format("True y", spectrum_true[0]), linewidth=4)
ax2.legend(fontsize='large')
ax2.set_xlim(frq_range[1], frq_range[-1])
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")
ax2.set_title("Frequency Responses for the all components")
# plt.show()
__auto_show__(plt.show())

# --- Code cell 380 ---
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from PFFRA import PermFeatureFreqRespoAnalysis  # Assuming you have the PFFRA module

# Assuming df_USA contains the features and target variable
# X should contain the features, and y should contain the target variable

# Selecting the features of interest
selected_features = [ 'Manufacturing_JAPAN', 'Trade_Balance_JAPAN', 'GovtExp_JAPAN']  # Include GDP_USA as the target variable
X_selected = df_Japan[selected_features]
y = df_Japan['GDP_JAPAN']  # Target variable is GDP_USA

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Instantiate PFFRA for investigating frequency response
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)

# Investigate multiple features and output their permutation spectrum data
for i in range(X_selected.shape[1]):
    # Instantiate PFFRA for the current feature
    pffra = PermFeatureFreqRespoAnalysis(y=y, X=X_selected, model=model, interested_feature_index=i)
    
    # Generate permutation dataset
    X_interested_feature, X_other_feature = pffra.permuted_dataset(mode='mean')
    
    # Predict target variables using the permutated datasets
    pred_interested_feature, pred_other_feature, pred_all_feature = pffra.permu_pred(X_interested_feature, X_other_feature)
    
    # Calculate the sampling frequency of your time series data
    sampling_frequency = len(y)  # Assuming each data point corresponds to 1 unit of time

    # Calculate the Nyquist frequency (half of the sampling frequency)
    nyquist_frequency = sampling_frequency / 2

    # Define the frequency range based on the Nyquist frequency
    frequency_range = np.linspace(0, nyquist_frequency, num=len(y) // 2)
    
    # Generate spectrums for analysis with the appropriate sample_rate
    spectrums = pffra.gen_spectrum(pred_interested_feature=pred_interested_feature, 
                                    pred_other_feature=pred_other_feature, 
                                    pred_all_feature=pred_all_feature, 
                                    sample_rate=sampling_frequency)
    
    # Unpack spectrums
    spectrum_interested_i = spectrums[0]
    spectrum_all = spectrums[2]
    spectrum_true = spectrums[3]
    frq_range = spectrums[4]
    
    # Plot permuted frequency responses for each component
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.titlesize"] = 16  
    plt.rcParams["xtick.labelsize"] = "large"
    plt.rcParams["ytick.labelsize"] = "large"
    
    ax1.plot(frq_range[1:], spectrum_interested_i[1:], 
             label="x_{} (DC: {:.2f})".format(i, spectrum_interested_i[0]))
    ax1.legend()
    ax1.set_xlabel("Frequency (Hz)")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Permuted Frequency Responses for each component")

ax2 = fig.add_subplot(122)
ax2.plot(frq_range[1:], spectrum_all[1:], 
         label="{} (DC: {:.2e})".format("all features", spectrum_all[0]))
ax2.plot(frq_range[1:], spectrum_true[1:], 
         label="{} (DC: {:.2e})".format("True y", spectrum_true[0]))
ax2.legend()
ax2.set_xlim(frq_range[1], frq_range[-1])
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")
ax2.set_title("Frequency Responses for the all components")
# plt.show()
__auto_show__(plt.show())

# --- Markdown cell 381 ---
# # Results - Visualisation

# --- Code cell 382 ---
import numpy as np
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'UK', 'China', 'Japan']
lstm_accuracies = [89.964, 81.682, 82.188, 80.971]  # Replace with actual LSTM accuracies
ts_accuracies = [85.05, 91.25, 87.18, 91.39]         # Replace with actual Time Series Analysis accuracies

# Set the width of the bars
bar_width = 0.35

# Set the positions of the bars on the x-axis
r1 = np.arange(len(countries))
r2 = [x + bar_width for x in r1]

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(r1, lstm_accuracies, color='#88CCEE', width=bar_width, edgecolor='grey')
plt.bar(r2, ts_accuracies, color='#117733', width=bar_width, edgecolor='grey')

# Add xticks on the middle of the group bars
plt.xlabel('Country', fontweight='bold')
plt.ylabel('Accuracy (%)', fontweight='bold')
plt.xticks([r + bar_width/2 for r in range(len(countries))], countries)

# Add labels and title
plt.title('LSTM V/S TIME SERIES ANALYSIS', fontweight='bold')

# Add "LSTM" and "TSA" on top of bars
for i in range(len(countries)):
    plt.text(r1[i], lstm_accuracies[i] + 1, 'LSTM', color='black', ha='center', fontweight='bold')
    plt.text(r2[i], ts_accuracies[i] + 1, 'TSA', color='black', ha='center', fontweight='bold')

# Show plot
plt.tight_layout()
# plt.show()
__auto_show__(plt.show())

# --- Code cell 383 ---
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'UK', 'China', 'Japan']
dataframes = [df_USA, df_UK, df_China, df_Japan]
colors = ['#44AA99', '#332288', '#AA4499', '#CC6677']  # Updated colors

# Create the plot
plt.figure(figsize=(12, 8))

# Plot GDP for each country
for country, df, color in zip(countries, dataframes, colors):
    plt.plot(df.index, df['GDP_' + country.upper()], color=color, label=country, linewidth=5)  # Increase linewidth for bold curves

# Add labels and title
plt.xlabel('Year', fontsize=20)  # Adjust fontsize here
plt.ylabel('GDP (Million Dollars)', fontsize=20)
plt.title('GDP Trends for Different Countries', fontsize=20)
plt.xticks(rotation=45)
plt.tight_layout()

# Add legend inside the plot
plt.legend(loc='upper left', fontsize=20)  # Increase legend fontsize

# Remove grid
plt.grid(False)

# Show the plot
# plt.show()
__auto_show__(plt.show())

# --- Code cell 384 ---
import pandas as pd

# Data
data = {
    'Country': ['China', 'Japan', 'UK', 'USA'],
    'LSTM RMSE': [3255896.2649991377, 745692.0277767156, 499066.88555892423, 1944026.6073306028],
    'LSTM Accuracy (%)': [80.63865879550461, 84.383, 83.256, 91.746],
    'ARIMA RMSE': [2242993.4231549664, 588398.2087718976, 242067.15043585186, 3538477.712988255],
    'ARIMA Accuracy (%)': [86.661, 87.677, 91.878, 84.977]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
# print(df)
__auto_show__(print(df))