x = tf.constant([[13, 1], [4, 0]], dtype=tf.float16)

mean_col = tf.reduce_mean(x, axis = 0)

print("Mean accross columns: ", mean_col)

"""
Mean accross columns:  tf.Tensor([8.5 0.5], shape=(2,), dtype=float16)

"""
