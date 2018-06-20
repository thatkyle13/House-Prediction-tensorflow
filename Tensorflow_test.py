#   import Tensorflow
import tensorflow as tf

sess = tf.Session()

# Verify we can print a string
hello = tf.constant("Hello World")
print(sess.run(hello))

#   Perform some simple math
a = tf.constant(22)
b = tf.constant(20)
print('a + b = {0}'.format(sess.run(a + b)))