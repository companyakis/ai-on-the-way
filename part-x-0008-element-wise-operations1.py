a = tf.Variable([1, 2, 3])

b = tf.Variable([3, 4, 5])

print(a + b)

print(a - b)

print(a * b)

print(a / b)

"""
tf.Tensor([4 6 8], shape=(3,), dtype=int32)

tf.Tensor([-2 -2 -2], shape=(3,), dtype=int32)

tf.Tensor([ 3  8 15], shape=(3,), dtype=int32)

tf.Tensor([0.33333333 0.5        0.6       ], shape=(3,), dtype=float64)

"""
