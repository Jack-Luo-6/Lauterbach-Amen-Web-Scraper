import pandas as pd 

df=pd.read_excel(r'C:\Users\jackl\Desktop\UChicago\Boutique Internship\Lauterbach & Amen\Accounting Firm M&A.xlsx')
within_region = []
outside_region = []
for i in range(0,501):
    if df.iloc[i][9][-2:] == df.iloc[i][10][-2:]:
        within_region.append(df.iloc[i][0])
    else:
        outside_region.append(df.iloc[i][0])
print(within_region, len(within_region)-1)
print(outside_region, len(outside_region)-1)