import pandas as pd
import os,argparse
import numpy as np

def pivot_excel(filename):
    the_file = pd.read_excel(filename)

    #setting index
    # the_file.set_index('shift', inplace=True)
    # print(the_file)
    print('************************Analysis of {}************************'.format(filename))
    print("\nThe file has: {} columns and {} rows of data.\n".format(len(the_file.columns), len(the_file.index)))
    print('Total Coal Production is: {} Tonnes.\n'.format(the_file['Coal dumped'].sum()))
    print('Total OB Production is: {} Cubic Metres.\n'.format(the_file['OB Dumped'].sum()))

    #groupby gives us a simple way to aggregate values
    #based on the entries of a specific column to generate summary statistics, etc
    #Note that whenever we are using group by, we need to apply some aggregate function on rest of the columns that are 
    # being selected.
    #Equivalent SQL Query: SELECT shift, SUM('Coal dumped'), SUM(OB Dumperd') FROM the_file GROUP BY shift;
    print('SHIFTWISE PRODUCTION TOTALS:\n')
    print(the_file[['shift', 'Coal dumped', 'OB Dumped']].groupby('shift').sum())
    print('\nSHIFTWISE TRIP COUNT TOTALS:\n')
    print(the_file[['shift', 'Dumper_Number_of_Trips']].groupby('shift').sum())
    print('\nPROCESS-ORDER WISE PRODUCTION TOTALS:\n')
    print(the_file[['Process_Order', 'Coal dumped', 'OB Dumped']].groupby('Process_Order').sum())
    
    #Remeber, in tables we are always representing data across two dimensions, (called index and columns in df).
    #So, by using group by, we simply change those two dimensions. And the column around which we are grouping,
    #now becomes the first dimenssion(horizontal) and the other columns selected to be displayed are the second
    #dimension. But since we have applied grouping on first dimension, we need to apply some sort of aggregation
    #on the second dimension too, like sum(), count(), average()
    
    # print('\n************Testing taking subset*************')
    # print(the_file[the_file['Coal dumped'] >= 500])
    
    #Pivot Tables
    # Pivot tables are a piece of summarized information that is generated from a large underlying dataset. 
    # It is generally used to report on specific dimensions from the vast datasets. Essentially, the user can 
    # convert rows into columns. This gives the users the ability to transpose columns from a SQL Server table 
    # easily and create reports as per the requirements. 

    print('\n************PIVOT TABLES*************\n')
    print('SHIFTWISE PRODUCTION TOTALS PER SEAM ------- OB\n')
    print(pd.pivot_table(the_file, values='OB Dumped', columns='shift', index='SEAM', aggfunc=np.sum))
    print('\nSHIFTWISE PRODUCTION TOTALS PER SEAM ------- Coal\n')
    print(pd.pivot_table(the_file, values='Coal dumped', columns=['SEAM'], index='shift', aggfunc=np.sum).fillna(0))
    print('\n')
    print(pd.pivot_table(the_file, values='Coal dumped', columns=['Process_Order'], index='shift', aggfunc=np.sum).fillna(0))
    print('\nSHIFTWISE PRODUCTION TOTALS PER SHOVEL------- Coal\n')
    print(pd.pivot_table(the_file, values='Coal dumped', columns=['Shovel_number'], index='shift', aggfunc=np.sum).fillna(0))
    print('\nDUMPYARD WISE PRODUCTION TOTALS PER SHOVEL------- Coal\n')
    print(pd.pivot_table(the_file, values='Coal dumped', columns=['Shovel_number'], index='DUMPYARD CODE', aggfunc=np.sum).fillna(0))

    #Linear Regression

if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('filename', help='The path of the excel file', type=str)
    args = argvparser.parse_args()
    pivot_excel(args.filename)