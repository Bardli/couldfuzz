import tensorflow as tf
try:
  x_tensor = tf.random.uniform([1, 399, 598, 3], dtype=tf.float32)
  x = tf.identity(x_tensor)
  y = -1024.0
  name = None
  results["res"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
