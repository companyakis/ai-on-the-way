import tensorflow as tf

# define-variables

v_0 = 2025

v_1 = tf.Variable(100)

v_2 = tf.Variable([121, -5])

v_3 = tf.Variable([[3, 6, 9], [12, 121, 1234]])

print(v_0)

print(v_1)

print(v_2)

print(v_3)


"""
2025
<tf.Variable 'Variable:0' shape=() dtype=int32, numpy=100>

<tf.Variable 'Variable:0' shape=(2,) dtype=int32, numpy=array([121,  -5], dtype=int32)>

<tf.Variable 'Variable:0' shape=(2, 3) dtype=int32, numpy=
array([[   3,    6,    9],
       [  12,  121, 1234]], dtype=int32)>


"""
