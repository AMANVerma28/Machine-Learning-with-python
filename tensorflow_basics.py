import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1,x2)
print(result)

with tf.Session() as sess:
    # output = sess.run(result)
    # print(output)
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.], [2.]])
    product = tf.matmul(matrix1, matrix2)
    print(sess.run(product))