x = tf.constant([[13, 1], [4, 0]], dtype=tf.float16)

mean_row = tf.reduce_mean(x, axis = 1)

print("Mean accross rows: ", mean_row)

"""
Mean accross rows:  tf.Tensor([7. 2.], shape=(2,), dtype=float16)

"""
