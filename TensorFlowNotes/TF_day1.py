'''
Build Graph tutorials: 
https://www.tensorflow.org/api_guides/python/framework#Core_graph_data_structures
'''

#Build a default graph
c = tf.constant(4.0)	# tf.constant() is an operator, which returns tensor as a constant object;
# 4.0 here is a parameter value; Operation could also take in tensor parameter 
assert c.graph is tf.get_default_graph()

g = tf.Graph()
with g.as_default():	#a context manager: set default grpah;
	c = tf.constant(30.0)
	assert c.graph is g		# call any operation, should produce tensors in default graph, unless otherwise specified
	

'''
https://www.tensorflow.org/api_docs/python/tf/Tensor
'''	
#Build a dataflow graph: all tensors below defined under default graph
# thus, tensor declaration/initialization == graph initialization
c = tf.constant([[1.0,2.0], [3.0, 4.0]])	# return a 2*2, 2d tensor
d = tf.constant([[1.0,1.0], [0.0, 1.0]])	# return a 2*2, 2d tensor
e = tf.matmul(c,d)		#an example of operation taken in two tensors are tensor parameter 

#create a session to execute the graph
sess = tf.Session()

#execute and graph, and store the value e returns in a result; e is an operation 
result = sess.run(e)	# session.run() accepts operation/ tensors as input parameter
# session.run() executes 1 computation at a time. 

a = tf.constant([10,20])
b = tf.constant([1.0,2.0])
v = session.run(a)
v = session.run({'k1':MyData(a,b), 'k2':[b,a]})

MyData = collections.namedtupe('MyData', ['a','b'])
   # v is a dict with
   # v['k1'] is a MyData namedtuple with 'a' (the numpy array [10, 20]) and
   # 'b' (the numpy array [1.0, 2.0])
   # v['k2'] is a list with the numpy array [1.0, 2.0] and the numpy array
   # [10, 20].
