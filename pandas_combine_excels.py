import os
import pandas as pd
from pandas.io.excel._base import read_excel

cwd = os.getcwd()
files = os.listdir(cwd)
excel_files = [x for x in files if x.endswith('.xlsx')]
combined_df = pd.concat([read_excel(x) for x in excel_files], ignore_index=True)
combined_df.to_excel('total_production.xlsx', index=False);