import tensorflow as tf
try:
  x_tensor = tf.random.uniform([1, 12, 26, 26], minval=-256, maxval=257, dtype=tf.int32)
  x = tf.identity(x_tensor)
  y_tensor = tf.random.uniform([], dtype=tf.float32)
  y = tf.identity(y_tensor)
  name = None
  results["res"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)