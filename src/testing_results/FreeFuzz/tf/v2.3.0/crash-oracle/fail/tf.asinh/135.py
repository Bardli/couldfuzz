import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([434, 384], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int16)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
