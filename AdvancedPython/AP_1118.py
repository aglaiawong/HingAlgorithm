'''
  Emulating switch/case statements in python with Dict
'''

def myfunc(a,b):
	return a+b
	
funcs[myfunc]
funcs[0](2,4)

func_dict = {
	'cond_a': handle_a,
	'cond_b': handle_b,
}

def dispatch_dict(operator, x, y):
	return {
		'add': lambda: x+y,		#lambda means return xxx
		'sub': lambda: x-y,
		'mul': lambda: x*y,
		'div': lambda: x/y,
	}.get(operator, lambda: None)()		#get() is a dict() operator
	
'''
clases: Built-In class attributes 
'''
class Employee:
	'Common base class for all employees'
	empCount = 0		#a class variable shared among all instances
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1		#updating global variable
	
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
	
	def displayEmployee(self):
		print "Name: ", self.name, ", Salary: ", self.salary

emp1 = Employee('Sandy', 1000)
emp1.displayEmployee()

Employee.__doc__	#doc for entire class 
Employee.__name__	#if __name__ == '__main__'
Employee.__module__		#the py file containing the class
Employee.__bases__		#base classes 
Employee.__dict__		#hold all properties of a class 

'''
if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''

#!/usr/bin/python

class GrandParent:
    GP_Attrib = 200
    def __init__(self):
        print "Grampa's class"

class Parent:        # define parent class
   parentAttr = 100
   __sexualOrientation = 'homosexual'
   # variable hiding: intended for use within class definition only
   # to access outside class, use: <instanceName>._<classN>__<secretAttributeN>
   
   
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent, GrandParent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

p = Parent()	  
c = Child()          # instance of child

c.parentMethod()     # calls parent's method
c.childMethod()      # child calls its method
c.setAttr(200)       # again call parent's method

#two ways to get parent attributes 
print(c.parentAttr)     #100
c.getAttr()          # again call parent's method

#all return true for the following
print(isinstance(c, Parent))
print(isinstance(c, Parent))
print(issubclass(Child, GrandParent))

print(c.__sexualOrientation)	#fail: no attribute
print(p.__sexualOrientation)	#fails still 
print(p._Parent__sexualOrientation)		#homosexual

'''
Base methods for overriding
'''
class Vector:
	def __init__(self, a,b):
		self.a = a
		self.b = b
	
	def __str__(self):
		return 'Vector: (%d, %d)' % (self.a, self.b)
	
	def __add__(self,other):	#override 'add' operator
		return Vector(self.a+other.a, self.b+other.b)

v1 = Vector(1,2)
v2 = Vector(5,-2)
print v1+v2


















