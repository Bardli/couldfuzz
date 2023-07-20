import tensorflow as tf
try:
  x_tensor = tf.random.uniform([3, 256], dtype=tf.float32)
  x = tf.identity(x_tensor)
  y = 3
  name = None
  results["res"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
