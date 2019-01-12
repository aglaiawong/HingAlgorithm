#-*-coding:utf-8-*-

import tensorflow as tf

sess = tf.InteractiveSession()
w1 = tf.Variable(tf.random_normal([2,3],mean=1.0,stddev=1.0))
w2 = tf.Variable(tf.random_normal([3,1],mean=1.0,stddev=1.0))

x=tf.constant([[0.7,0.9]])

tf.global_variables_initializer().run()
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

print(y)
print(y.eval())
