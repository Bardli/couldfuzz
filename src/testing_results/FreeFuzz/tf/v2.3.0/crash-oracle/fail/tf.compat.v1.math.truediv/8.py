import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([3, 1, 5, 5], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
  x = tf.identity(x_tensor)
  y_tensor = tf.random.uniform([], dtype=tf.float32)
  y = tf.identity(y_tensor)
  name = None
  results["res"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)