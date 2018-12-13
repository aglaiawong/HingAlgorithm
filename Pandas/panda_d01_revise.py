'''
Facts about pandas
- labelled array: Series and DataFrame
- memory-efficient sparse storage 
- data structures are operated in 'dictionary'-like manner
- favour immutability: values within data structures mutatable, but not size of ds
- immutability guarnateed: new objects generated instead of changing existing ones 
- 
'''

# check existence of index in a Series
my_obj2 = pd.Series([8,9,10,11], index=['a','b','c','d'])
'a' in my_obj2

#convert Dict into Series by calling Series constructor
dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 }
my_obj3 = pd.Series(dic_data)

registration = [True,False,True,True]
registration = pd.Series(registration)

'''
# my_obj3
birthday       1996-1-1
luckynumber           7
name              apple
dtype: object		-->When a Series contain heterogeneous data types in this field

# registration
0     True
1    False
2     True
3     True
dtype: bool
'''

'''
DataFrame
- column index starts with 0
- transpose of python list to give a column
- convert a dictionary to produce named columns 
- connection to numpy: index as axes 0, columns as axes 1
'''
data = {'name': ['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day':[11,23,8,3,11]}
myframe = pd.DataFrame(data)
myframe

# change columns order
myframe1 = pd.DataFrame(data, columns=['name', 'year', 'month', 'day'])

# new columns be assigned with NaN
myframe3 = pd.DataFrame(data, columns=['name', 'year', 'month', 'day', 'luckynumber'])

# fill the newly-formed, NaN columns with values 
# first convert list into Series
# then assign this new Series to the column
luckynumber = ['3','2','1','7','8']
luckynumber = pd.Series(luckynumber)

# iterate over columns 
for col in df.columns:	#return a immutable ndarray on column names 
	series = df[col]

# an example of dataframe generation 
dates = pd.date_range('20130101', periods=6)	#rtn: DatetimeIndex
'''
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
'''
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=list('ABCD'))
'''
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
'''


#BKMK: http://pandas.pydata.org/pandas-docs/stable/10min.html












