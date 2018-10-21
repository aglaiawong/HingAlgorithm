import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import tf
from tensorflow.examples.tutorials.mnist import input_data

# import MNIST data
mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

# Training parameters 
learning_rate = 0.01
num_steps = 30000
batch_size = 256

display_step = 1000		#? 
examples_to_show = 10

#network parameters 
num_hidden_1 = 256		#first layer num of features == input dimen
num_hidden_2 = 128
num_input = 784

X = tf.placeholder("float", [None, num_input])

# Math proof of weights and bias dimensions needed 
weights = {
	'encoder_h1': tf.Variable(tf.random_normal([num_input, num_hidden_1])),
	'encoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_hidden_2])),
	'decoder_h1': tf.Variable(tf.random_normal([num_hidden_2, num_hidden_1])),
	'decoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_input]))
}

biases = {
	'encoder_b1': tf.Variable(tf.random_normal([num_hidden_1])),
	'encoder_b2': tf.Variable(tf.random_normal([num_hidden_2])),
	'decoder_b1': tf.Variable(tf.random_normal([num_hidden_1])),
	'decoder_b2': tf.Variable(tf.random_normal([num_input])),
}

#Building the encoder
def encoder(X):
	# Encoder hidden layer with sigmoid activation #1
	layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),biases['encoder_b1']))
	
	# Encoder hidden layer with sigmoid activation #2
	layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),biases['encoder_b2']))
	return layer_2

#Building the decoder 	
def decoder(x):
	layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),biases['decoder_b1']))
	layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),biases['decoder_b2']))
	return layer_2
	
#construct the model
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)
#prediction
y_pred = decoder_op
#targets (labels) are the input data 
y_true = X 

#define the loss and ptimizer, minimize the squared error 
loss = tf.reduce_mean(tf.pow(y_true - y_pred),2)
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

#initialize the variables 
init = tf.global_variables_initializer()

# start training 
with tf.Session() as sess:
	# run initializer
	sess.run(init)
	
	for i in range(1, num_steps+1):
		batch_x, _ = mnist.train.next_batch(batch_size)
		_, l = sess.run([optimizer, loss], feed_dict={X: batch_x})
	#display logs per step 
		if i%display_step == 0 or i == 1:
			print('Step %i: Minibatch Loss: %f' % (i,l))
	
    # Testing
    # Encode and decode images from test set and visualize their reconstruction.
    n = 4
    canvas_orig = np.empty((28 * n, 28 * n))
    canvas_recon = np.empty((28 * n, 28 * n))
    for i in range(n):
        # MNIST test set
        batch_x, _ = mnist.test.next_batch(n)
        # Encode and decode the digit image
        g = sess.run(decoder_op, feed_dict={X: batch_x})

        # Display original images
        for j in range(n):
            # Draw the original digits
            canvas_orig[i * 28:(i + 1) * 28, j * 28:(j + 1) * 28] = \
                batch_x[j].reshape([28, 28])
        # Display reconstructed images
        for j in range(n):
            # Draw the reconstructed digits
            canvas_recon[i * 28:(i + 1) * 28, j * 28:(j + 1) * 28] = \
                g[j].reshape([28, 28])

    print("Original Images")
    plt.figure(figsize=(n, n))
    plt.imshow(canvas_orig, origin="upper", cmap="gray")
    plt.show()

    print("Reconstructed Images")
    plt.figure(figsize=(n, n))
    plt.imshow(canvas_recon, origin="upper", cmap="gray")
plt.show()
	
	
	
	

	

	
	
	
	
	
	
	
	
	
	
	
	
	


