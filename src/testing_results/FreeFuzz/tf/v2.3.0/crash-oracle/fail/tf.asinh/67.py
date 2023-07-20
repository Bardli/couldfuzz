import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([436, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
