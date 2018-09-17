# Tensor: represent results of operation that will be run 
a = tf.constant(3.0, dtype=tf.float32)
print(a)
Tensor("Const:0", shape=(), dtype=float32)
# tf.constant() construct a handle, a tensor object which is part of the graph; i.e. operation ONLY BUILDS A COMPUTATIONAL GRAPH
# each operation in graph has unique name 



# TensorBoard: visualize computational graph
writer = tf.summary.FileWriter('/Documents')
writer.add_graph(tf.get_default_graph())


'''
For each call on run(), only a consistent value produced. 
i.e. during a call to tf.Session.run any tf.Tensor only has a single value
'''
vec = tf.random_uniform(shape=(3,))		#a 3-d vector of random val
out1 = vec + 1
out2 = vec + 2
print(sess.run(vec))	# diff values for each call 
print(sess.run(vec))
print(sess.run((out1, out2)))	#same set of random values returned 

'''
Feeding by placeholder
- parameterized a graph 
- for providing value to a variable later 
'''
x = tf.placeholder(tf.float32)  	#build graph by init a tensor
y = tf.placeholder(tf.float32)
z = x + y 		#build graph by operation

#feeding at run()
sess.run(z, feed_dict={x:3, y:4.5})		#7.5
sess.run(z, feed_dict={x:[1,3], y:[2,4]})		#[ 3.  7.]


'''
Datasets: stream data into a model 
- provide a tensor
- create dataset from tensor 
- create an iterator to read from dataset
'''
my_data = [
    [0, 1,],
    [2, 3,],
    [4, 5,],
    [6, 7,],
]
slices = tf.data.Dataset.from_tensor_slices(my_data)	#build dataset from slicing tensor
iterator = slices.make_one_shot_iterator()	#initialize an iterator to read dataset; 
#one-shot iterator only supports iterating via dataset one time only
next_item = iterator.get_next()
# loop to read samples from iterator
while True:
	try:
		print(sess.run(next_item))
	except tf.errors.OutOfRangeError:	#when iterator reaches the end of the data stream 
		break

'''
one-shot vs initializable iterator
- latter allows parameterization the definition of dataset 
'''
# non-parameterizable iterator: one-shot 
dataset = tf.data.Dataset.range(100)
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()
for i in range(100):
	value = sess.run(next_element)
	assert i == value
	
# parameterizable iterator: initializable iterator
max_value = tf.placeholder(tf.int64, shape=[])
dataset = tf.data.Dataset.range(max_value)		#parameterized dataset
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()
sess.run(iterator.initializer, feed_dict={max_value:10})
for i in range(10):
	value = sess.run(next_element)
	assert i == value

'''
Layers: add trainable parameters to a graph 
- package both variables and operations acting on them
'''
x = tf.placeholder(tf.float32, shape=[None,3])
linear_model = tf.layers.Dense(units=1)		#output dimension=1
# for each input of size (,3) in an array, do layers operation
y = linear_model(x)

# variables in a layer must be initialized before use 
init = tf.global_variables_initializer()	#this operation only returns a handle to operation
sess.run(init)	#from the handle, run() initializesthe global variable;





'''
BKMK: https://www.tensorflow.org/guide/low_level_intro
@ feature columns 
'''








































