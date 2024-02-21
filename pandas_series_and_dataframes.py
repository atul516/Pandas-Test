import pandas
data = {"id": {'a': 78,'b' : 42,'c' : 12,'d' : 86}, "Name": {'a' : "Bob", 'b' : "Karen", 'c' : "Kate", 'd' : "Bill"}}
data1 = [[1,2],[3,{"a":"b"},3]]
data2= [10,20,30,40,50,60]
data3= [[10,6]]
data4 = [{'a': 1, 'b': 2, 'c': 3},
         {'a': 10, 'b': 20, 'c': 30}]
data5={
    "id" : [1,4,7,9],
    "name" : ['a','b','c','d']
}
# print(data)
# print(data['id'])
# print(data['Name'])
# print('------------------------------------------------------------------------')
# series = pandas.Series(data3)
#Pandas Series data structure is a one-dimensional labelled array.
#Pandas Series can be instantiated with a list or dict.. both!
# print(series.ndim)
# print(series)
# print(series['Name']['a'])
# print(series[1][0][0])
# print('------------------------------------------------------------------------')
#Series can only contain single list with index, whereas dataframe can be made of more than one series.
#The name of a Series becomes its index or column name if it is used to form a DataFrame.
#It is also used whenever displaying the Series using the interpreter.
#Pandas DataFrame is a two-dimensional data structure composed of columns and rows.
#You can think of the DataFrame as similar to a CSV or relational database table.
#For the dataFrame, all arrays must be of the same length, otherwise NaN tyoe values will be inserted.
#DataFrame() function is used to create a dataframe in Pandas. The syntax of creating dataframe is:
#pandas.DataFrame(data, index, columns)
#data: It is a dataset from which dataframe is to be created. It can be list, dictionary, scalar value, series, ndarrays, etc.
#One way of looking at it is that DataFrames are essentially groups of individual Series, column wise
#Each Series can have it's own datatype dtype.
# If we initialise a dataframe with single un-nested list, then the list values are taken as a single column and different rows.
# If we initialize a dataframe with a python list within lists, inner lists are taken as rows of the table.
# Hint: So in case of nested lists we can refer to elements as li[i][j], where i is top most index, and j
# is the first nested index. So for the dataframe, i represents index/row numbering and j is column numbering.
# That's why, in case of a single-dimensional list, the li[i] is seen as a single column, with i representing index/row numbering.
# On the other hand, if we initialize using a dictionary, its top-most key-set is taken as columns names, 
# then index names, then mere data.
# So, when creating dataframe from a dictionary containing lists which provides column names anyways, 
# we can provide index label explicitly in the dataframe constructor or later also as df.index = [...].
# index: It is optional, by default the index of the dataframe starts from 0 and ends at the last data value(n-1). 
# It defines the row label explicitly.
# columns: This parameter is used to provide column names in the dataframe.If the column name is not defined by default, it will take a value from 0 to n-1.
# df = pandas.DataFrame(data5)
# print(df)
# print(type(df))
# print(df.dtypes)
# print(df.info())
#Subsetting can extract a particular series from a dataframe
# print(df['id'])
# print(df.index)
# print(df.columns)
#see dataframe's rowsxcolumns
# print(df.shape)
# print(type(df.shape))
#no. of dimensions
# print(df.ndim)
#we can edit column names and index names
# df.columns = ['Identity','Full Names']
# df.index = ["row" + str(i) for i in range(4)]
# print(df)
# print(df['Identity'])
# print('--------------------------------------------------------------------------------------')
#The loc and iloc function
# print(df.iloc[:2])
# print(df.loc[:])
#Here's how to traverse a dataframe with multiindex using a subset of the index
# for i in inc.index:
#     print(inc.loc[[i[0]],['Dumper_Trips','Standard_Trips']])
#     or
#     print(inc['Dumper_Trips'][i[0]])
#     print(inc['Dumper_Trips'][i])

#Here's how to traverse a dataframe row wise efficiently
# for row in inc.itertuples():
#     print(row)


def append_row_to_dataframe(df, row):
    df.loc[len(df)] = row

df = pandas.DataFrame(columns=['a','b','c'])
# Define a new row to be appended
row = [1, 2, 3]

# Append the row to the DataFrame
append_row_to_dataframe(df, row)

# Print the updated DataFrame
print(df)
