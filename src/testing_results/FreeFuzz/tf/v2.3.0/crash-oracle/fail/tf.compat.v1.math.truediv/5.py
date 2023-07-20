import tensorflow as tf
try:
  x_tensor = tf.random.uniform([1, 1, 16, 16], dtype=tf.float32)
  x = tf.identity(x_tensor)
  y_tensor = tf.saturate_cast(tf.random.uniform([], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
  y = tf.identity(y_tensor)
  name = None
  results["res"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
