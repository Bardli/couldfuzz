import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([358, 512], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
  x = tf.identity(x_tensor)
  results["res"] = tf.compat.v1.tan(x=x,)
except Exception as e:
  results["err"] = "Error:"+str(e)
