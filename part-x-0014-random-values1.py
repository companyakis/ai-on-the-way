tf.random.set_seed(2025)

data1 = tf.random.normal(shape = (4, 4), mean = 12, stddev = 2, dtype = tf.float16)

print(data1)

"""
tf.Tensor(
[[12.77  13.     9.17  12.59 ]
 [11.93   9.72  17.44  12.836]
 [12.22  11.13  12.76  11.72 ]
 [11.87  11.484 11.82  14.305]], shape=(4, 4), dtype=float16)

"""
