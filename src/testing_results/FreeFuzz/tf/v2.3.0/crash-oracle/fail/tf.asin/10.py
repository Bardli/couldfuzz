import tensorflow as tf
try:
  x_tensor = tf.random.uniform([436, 383], minval=-256, maxval=257, dtype=tf.int64)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asin(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
