import tensorflow as tf
import numpy as np

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 500)) # 随机输入
y_data = np.dot([0.100, 0.200], x_data) + np.array([0.30,0.40], ndmin=2).T

# 构造一个线性模型
#
b = tf.Variable(tf.zeros([2,1]))
W = tf.Variable(tf.random_uniform([1, 2], -10.0, 10.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 400):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))


# d = np.arange(1,10).reshape(3,3)
# #e = d[::-1]
# e = np.arange(10,19).reshape(3,3)
# print(np.dot(d,e))

SystemExit(0)

# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]