a = tf.Variable([[1, 2, 3], [4, 5, 6]])

b = tf.transpose(a)

print(b)

"""
tf.Tensor(
[[1 4]
 [2 5]
 [3 6]], 
 shape=(3, 2), dtype=int32)

"""
