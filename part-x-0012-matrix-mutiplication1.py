x = tf.constant([[3, 1], [4, 0]])

y = tf.constant([[2, 0], [1, 1]])

print(tf.matmul(x, y))

"""
3*2 + 1*1  3*0 + 1*1
4*2 + 0*1  4*0 + 0*1
"""

"""
tf.Tensor(
[[7 1]
 [8 0]], shape=(2, 2), dtype=int32)

"""
