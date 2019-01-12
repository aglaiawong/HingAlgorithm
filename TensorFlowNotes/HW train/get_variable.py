#-*-coding:utf-8-*-

import tensorflow as tf

tf.reset_default_graph()

var1 = tf.Variable(10.0, name="varname")
var2 = tf.Variable(11.0, name="varname")
var3 = tf.Variable(12.0)
var4 = tf.Variable(13.0)

with tf.variable_scope("test1"):
	var5 = tf.get_variable("varname", shape=[2], dtype=tf.float32)

with tf.variable_scope("test2"):
	var6 = tf.get_variable("varname", shape=[2], dtype=tf.float32)

print(var1.name)
print(var2.name)
print(var3.name)
print(var4.name)
print(var5.name)
print(var6.name)





