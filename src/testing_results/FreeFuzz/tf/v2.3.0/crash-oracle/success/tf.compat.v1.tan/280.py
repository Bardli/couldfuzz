import tensorflow as tf
try:
  x_tensor = tf.random.uniform([50, 1], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)