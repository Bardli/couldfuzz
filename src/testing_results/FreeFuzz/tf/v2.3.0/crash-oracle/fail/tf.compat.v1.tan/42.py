import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([2, 50], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)