import tensorflow as tf
try:
  x_tensor = tf.random.uniform([2, 12, 16, 16], dtype=tf.float16)
  x = tf.identity(x_tensor)
  y_tensor = tf.random.uniform([], dtype=tf.float32)
  y = tf.identity(y_tensor)
  name = None
  results["res"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)