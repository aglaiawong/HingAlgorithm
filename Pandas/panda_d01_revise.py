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


# inspect column dtypes in dataframe 
df.dtypes

# quick statistics on each column 
df.describe()

# transpose columns and index
df.T
'''
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
'''

# sort column: for attributes with sortable names 
df.sort_index(axis=1, ascending=False)
'''
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
'''

# sort each row by values in a particular column 
df.sort_values(by='B')	#by column name 
'''
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
'''

# selecting a column == yields a series 
df['A']
'''
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.673690
Freq: D, Name: A, dtype: float64
'''

# with datetime index, select via [] get rows 
df['20130102':'20130104']
'''
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
'''

#slicing, both endpoints included
df.loc['20130102':'20130104',['A','B']]		#use a list to hold different columns 

# get particular value for a field 
df.loc[dates[0],'A']	#loc[] accessed by name 
df.iloc[1,1]			#iloc[] accessed by index/numbers

#locate by list of index 
df.iloc[[1,2,4],[0,2]]]		#0=A, 2=C

'''
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
'''

# select by boolean
df[df.A > 0]
df[df > 0]		#check each value in df one by one;
# those smaller than zero automatically becomes NaN  
'''
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
'''
# operate on each value 
df2[df2>0] = -df2	#on RHS: entire df, each element negated 
# on LHS: only those rows with at least one value >0 in any columns are returned 


# only select ENTIRE row if one has 'two'/'four' in column 'E'
# the outtermost 'df2': select the entire rows 
df2[df2['E'].isin(['two','four'])]
'''
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
'''

# set value by label
df.at[dates[0], 'A'] = 0
# set value by position 
df.iat[0,1] = 0
# bunch setting of values for a column 
df.loc[:, 'D'] = np.array([5]*len(df))

#drop rows with missing data, NaN
df1.dropna(how='any')	#have NaN in any field 

# replace NaN with values 
df1.fillna(value=5)

# inspect where the NaN are 
pdf.isna(df1)

# calculate cumulative values within a column 
df.apply(np.cumsum)		#default axis=0, apply fnc on each column 
'''
                   A         B         C   D     F
2013-01-01  0.000000  0.000000 -1.509059   5   NaN
2013-01-02  1.212112 -0.173215 -1.389850  10   1.0
2013-01-03  0.350263 -2.277784 -1.884779  15   3.0
2013-01-04  1.071818 -2.984555 -2.924354  20   6.0
2013-01-05  0.646846 -2.417535 -2.648122  25  10.0
2013-01-06 -0.026844 -2.303886 -4.126549  30  15.0
'''

# apply fnc to each column 
df.apply(lambda x: x.max() - x.min())
'''
A    2.073961
B    2.671590
C    1.785291
D    0.000000
F    4.000000
dtype: float64
'''

# join by key
left = pd.DataFrame({'key':['foo', 'bar'], 'lval':[1,2]})	#convert Dict into df
right = pd.DataFrame({'key':['foo', 'bar'], 'rval':[4,5]})
pd.merge(left, right, on='key')

'''
Grouping in Pandas
i) splitting the data 
ii) applying some fnc 
iii) combining 
'''

#group by multi-index
df.groupby(['A','B']).sum()
'''
                  C         D
A   B                        
bar one   -1.814470  2.395985
    three -0.595447  0.166599
    two   -0.392670 -0.136473
foo one   -1.195665 -0.616981
    three  1.928123 -1.623033
    two    2.414034  1.600434
'''

# time series 
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0,500, len(rng)), index=rng)
ts.resample('5Min').sum()

#http://pandas.pydata.org/pandas-docs/stable/10min.html#categoricals























