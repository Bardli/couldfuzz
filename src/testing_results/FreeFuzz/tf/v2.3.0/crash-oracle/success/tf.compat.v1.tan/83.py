import tensorflow as tf
try:
  x_tensor = tf.random.uniform([386, 512], dtype=tf.float32)
  x = tf.identity(x_tensor)
  results["res"] = tf.compat.v1.tan(x=x,)
except Exception as e:
  results["err"] = "Error:"+str(e)
