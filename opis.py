import glob as g
import pandas as pd

path = r'L:/SharedData/Denver/SupChnMgmt/General/OPIS Daily Fuel'
all_files = g.glob(path + "/*EOD.csv")

dfs = [pd.read_csv(fp) for fp in all_files]
df = pd.concat(dfs, ignore_index=True)
prod_ind_d = df['Product Indicator'] == 'D'
df = df[prod_ind_d]
print (df)


with pd.ExcelWriter('summary_test.xlsx') as writer:
    df.to_excel(writer)

