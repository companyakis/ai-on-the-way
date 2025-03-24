a = tf.Variable([[1, 2, 3], [4, 5, 6]])

b = tf.cast(a, dtype = tf.float16)

print(b)

"""
tf.Tensor(
[[1. 2. 3.]
 [4. 5. 6.]], shape=(2, 3), dtype=float16)

"""
