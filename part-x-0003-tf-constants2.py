# products => product ID, product price and cost per item and sales quantity

products_data = [
    [1, 25, 17.55, 300],
    [21, 16, 12.48, 424], 
    [65, 32.5, 26.8, 214], 
    [76, 17, 13.56, 654], 
    [77, 98, 90, 200], 
]

products_data_tensor = tf.constant(products_data)

print(products_data_tensor)

"""
tf.Tensor(
[[  1.    25.    17.55 300.  ]
 [ 21.    16.    12.48 424.  ]
 [ 65.    32.5   26.8  214.  ]
 [ 76.    17.    13.56 654.  ]
 [ 77.    98.    90.   200.  ]], shape=(5, 4), dtype=float32)

"""
