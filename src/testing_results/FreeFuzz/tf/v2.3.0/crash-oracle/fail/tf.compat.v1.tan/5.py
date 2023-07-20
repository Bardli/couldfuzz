import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([10000, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int16)
  x = tf.identity(x_tensor)
  results["res"] = tf.compat.v1.tan(x=x,)
except Exception as e:
  results["err"] = "Error:"+str(e)
