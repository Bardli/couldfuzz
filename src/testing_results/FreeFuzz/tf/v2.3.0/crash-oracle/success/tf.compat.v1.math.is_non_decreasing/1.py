import tensorflow as tf
try:
  x_tensor = tf.random.uniform([3], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.compat.v1.math.is_non_decreasing(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
