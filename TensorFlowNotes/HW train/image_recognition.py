from skimage import io, transform
import glob
import os
import tensorflow as tf
import numpy as np
import time

path = 'flower_photos/'
model_path='Model/model.ckpt'		#to saved model

#size of processed img
w=100
h=100
c=3

def read_img(path):
	cate = [path+x for x in os.listdir(path) if os.path.isdir(path+x)]
	
	# init separate holders for images and labels 
	imgs = []
	labels = []
	
	for idx, flower in enumerate(cate):
		for im in glob.glob(folder+'/*.jpg'):
			img=io.imread(im)
			img=transform.resize(img, (w,h))
			imgs.append(img)
			labels.append(idx)
	return np.asarray(imgs, np.float32), np.asarray(labels, np.int32)
	
data, label = read_img(path)
print("shape of data: %s"%(data.shape))
print("shape of data: %s"%(label.shape))

#shuffling, as usual 
num_example = data.shape[0]
arr = np.arange(num_example)
np.random.shuffle(arr)		#inplace shuffling
data = data[arr]	# shuffle dataset by by shuffled indices 
label = label[arr]

ratio = 0.8		#proportion for training data set
s=np.int(num_example*ratio)
x_train = data[:s]
y_train = data[:s]
x_val = data[s:]
y_val = label[s:]

x = tf.placeholder(tf.flaot, shpae=[None, w,h,c], name='x')
y_ = tf.placeholder(tf.int32, shpae=[None,], name='y_')



def model(input_tensor, train, regularizer):
'''
BASIC_STRUCTURE
- layers: conv + pooling layers 
- within each scope: weight, bias, conv/pool layer, activation fnc 
'''

	with tf.variable_scope('layer1-conv1'):
		#从截断的正态分布中输出随机值: 生成的值服从具有指定平均值和标准偏差的正态分布，如果生成的值大于平均值2个标准偏差的值则丢弃重新选择。
		#[w,h,#hidden,#output]
		conv1_weights = tf.get_variable("weight", [5,5,3,32], initializer=tf.truncated_normal_initializer(stddev=0.1))		#create new variable under current namescope 
		conv1_biases - tf.get_variable("bias", [32], initializer=tf.constant_initializer(0.0))
		
		conv1 = tf.nn.conv2d(input_tensor, convl_weights, strides=[1,1,1,1], padding='SAME')
		relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))
		
	with tf.name_scope("layer2-pool1"):
		pool1 = tf.nn.max_pool(relu1, ksize=[1,2,2,1], strides=[1,2,2,1], padding='VALID')	#return a tensor as well 
		# padding: valid vs same: https://stackoverflow.com/questions/37674306/what-is-the-difference-between-same-and-valid-padding-in-tf-nn-max-pool-of-t
	
	with tf.variable_scope("layer3-conv2"):
		conv2_weights = tf.get_variable("weight", [5,5,32,64], initializer=tf.truncated_normal_initializer(stddev=0.1))
		conv2_bias = tf.get_variable("biases", [64], initializer=tf.constant_initializer(0.0))
		#conv2 get the output of previous layer, which is pool1
		conv2 = tf.nn.conv2d(pool1, conv2_weights, stride=[1,1,1,1], padding='SAME')
		relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))
		
	with tf.name_scope("layer4-pool2"):
		pool2 = tf.nn.max_pool(relu2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='VALID')
	
	with tf.variable_scope("layer5-conv3"):
		


































		
