import tensorflow as tf
try:
  x_tensor = tf.cast(tf.random.uniform([1], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  x = tf.identity(x_tensor)
  y_tensor = tf.cast(tf.random.uniform([4], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  y = tf.identity(y_tensor)
  name = None
  results["res"] = tf.logical_and(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
