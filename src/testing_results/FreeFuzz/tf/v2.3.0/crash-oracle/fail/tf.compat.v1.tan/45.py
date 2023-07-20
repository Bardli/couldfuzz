import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([374, 511, 1], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
