import numpy as np
y = np.asarray(['Java', 'C++', 'Other language', 'Python', 'C++', 'Python'])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_numeric = le.fit_transform(y)
# whenever convert encoding: use fit_transform()

'''
In [220]: y_numeric
Out[220]: array([1, 0, 2, 3, 0, 3], dtype=int64)
'''

le.classes_
'''
In [221]: le.classes_
Out[221]: 
array(['C++', 'Java', 'Other language', 'Python'], 
      dtype='|S14')
'''


https://stackoverflow.com/questions/42819460/what-is-the-difference-between-onevsrestclassifier-and-multioutputclassifier-in
