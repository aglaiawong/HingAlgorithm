'''
TOPIC: class in python
'''

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def myfunc(self):
		print("hello my name is: " + self.name)

p1 = Person("John", 36)
print(p1.name)
print(p2.age)
p1.myfunc()
del p1		#del删除的是变量，而不是数据。

from base.base_model import BaseModel	#from <dir.fileName> import <className>
from base.base_train import BaseTrain


