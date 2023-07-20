import tensorflow as tf
try:
  x_tensor = tf.cast(tf.random.uniform([424, 512], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
