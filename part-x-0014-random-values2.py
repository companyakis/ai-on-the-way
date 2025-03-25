tf.random.set_seed(2025)

data2 = tf.random.uniform(shape = (4, 3), minval = 3, maxval = 12, dtype = tf.int32)

print(data2)

"""
tf.Tensor(
[[ 5  4  5]
 [ 5  6  7]
 [10  5 11]
 [ 6  4  5]], shape=(4, 3), dtype=int32)

"""
