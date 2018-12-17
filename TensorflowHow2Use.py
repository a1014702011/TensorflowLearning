import tensorflow as tf

constMatrixl1 = tf.constant(9999,shape = [9999,9999])
constMatrixl2 = tf.constant(9999,shape = [9999,999])
# variA = tf.Variable(tf.random_uniform_initializer([5,5],minval=0.0,maxval=99.0,dtype=tf.float32,seed=1234,name="variA"))
# variA = tf.Variable(tf.random_uniform([5,5],minval=0.0,maxval=99.0,dtype=tf.float32,seed=1234,name="variA"))
result = tf.matmul(constMatrixl1,constMatrixl2)
sess = tf.Session()
print(sess.run(result))
sess.close()