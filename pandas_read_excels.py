import os, argparse
import pandas

def read_excel(filename):
    #By default, __read_excel__ reads the first spreadsheet
    #read_excel returns a dataframe object containing the data of the file
    #if you don't use na_filter=false, then empty strings will be replaced with NaN
    #the_file = pandas.read_excel(filename, na_filter=false)
    #OR
    full_file = pandas.ExcelFile(filename)
    # print(full_file.sheet_names)
    the_file = full_file.parse('Sheet1')
    #parse supports most of the parameters available for read_excel
    
    # print(the_file.shape)
    # print(the_file.index)
    # print(the_file.columns)
    # print(the_file.ndim)
    # print(len(the_file))
    # print(the_file.head(45))
    # print(the_file.tail(5))
    # print(the_file.keys())
    # print(the_file.info())
    # print(len(the_file))

    #Accessing by rows:------------------------>
    #Ranges can also be used with iloc and loc with the important difference that loc automatically
    # includes the last value of the range, while iloc does not
    # print(the_file.iloc[34][5])
    # print(the_file.iloc[34,5])
    # print(the_file.iloc[34:42])
    # print(the_file.iloc[34].Operator)
    # print(the_file.loc[34, 'Operator'])
    # print(the_file.loc[34])

    #Accessing by columns:------------------------>
    #Since each column is just a numpy array, we can easily manipulate the values and create new columns
    # the_file['Coal dumped+20'] = the_file['Coal dumped'] + 20
    # print(the_file['Coal dumped'])
    # print(the_file[['Coal dumped','Coal dumped+20']])
        
    #we can edit column names and index names
    # df.columns = ['Identity','Full Names']
    # the_file.index = ["row" + str(i) for i in range(len(the_file)]

    #convert inner stuff to string
    #the_file_str = the_file.astype('string')
    
    #We can use .map(some function) and .transform(some function) on a Series and Dataframe respecdtively
    #to apply an operation to each element of that series or dataframe
    
    #covert to csv
    # the_file_str_lines_list = the_file.to_string(header=True, index=False, index_names=False).split('\n')
    # print(the_file_str_lines_list[0])
    # print(the_file_str_lines_list[1])
    # the_file_csv = '\n'.join([','.join(x.split()) for x in the_file_str_lines_list])
    # # open an output file in write mode
    # out_file = open('filedata', 'w')
    # out_file.write(the_file_csv.replace('NaN', ''))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('excel_file', help='The path of the excel file', type=str)
    args = parser.parse_args()
    read_excel(args.excel_file)